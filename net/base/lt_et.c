#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <strings.h>
#include <assert.h>
#include <unistd.h>
#include <errno.h>
#include <sys/types.h>
#include <sys/socket.h>
#include <arpa/inet.h>
#include <netinet/in.h>
#include <fcntl.h>
#include <sys/epoll.h>
#include <pthread.h>
#include <stdbool.h>
#include <libgen.h>


#define MAX_EVENT_NUMBER 1024
#define BUF_SIZE 10


int setnonblocking(int fd)
{
	int old_option = fcntl(fd, F_GETFL);
	int new_option = old_option | O_NONBLOCK;

	fcntl(fd, F_SETFL, new_option);
	return old_option;
}

void addfd(int epoll_fd, int fd, bool enable_et)
{
	struct epoll_event event;

	event.data.fd = fd;
	event.events =EPOLLIN;
	if(enable_et)
	{
		event.events |= EPOLLET;
	}
	epoll_ctl(epoll_fd, EPOLL_CTL_ADD, fd, &event);
	setnonblocking(fd);
}

void lt(struct epoll_event *events, int number, int epollfd,  int listenfd)
{
	char buf[BUF_SIZE];
	
	for(int i = 0; i < number; i++)
	{
		int sockfd =events[i].data.fd;

		if(sockfd == listenfd)
		{
			struct sockaddr_in client;
			socklen_t client_addrlength = sizeof(client);
			int connfd = accept(listenfd, (struct sockaddr *)&client_addrlength, &client_addrlength);
			addfd(epollfd, connfd, false);
		}
		else if(events[i].events & EPOLLIN)
		{
			printf("event trigger once \n");
			memset(buf, 0, BUF_SIZE);
			int ret = recv(sockfd, buf, BUF_SIZE, 0);

			if(ret <= 0)
			{
				close(sockfd);
				continue;
			}

			printf("Get %d bytes of content : %s \n", ret, buf);
		}
		else
		{
			printf("Something else haappened\n");
		}
	}

}

void et(struct epoll_event *events, int number, int epollfd, int listenfd)
{
	char buf[BUF_SIZE];

	for(int i = 0; i < number; i++)
	{
		int socketfd = events[i].data.fd;

		if(socketfd == listenfd)
		{
			struct sockaddr_in client_address;
			socklen_t client_addrlen = sizeof(client_address);

			int connfd = accept(listenfd, (struct sockaddr*)&client_address, &client_addrlen);
			addfd(epollfd, connfd, true);
		}
		else if(events[i].events & EPOLLIN)
		{
			//ET模式下这段代码不会重复触发，需循环读取数据，以确保socket读缓存中的所有数据读出
			printf("event trigger once \n");
			while(1)
			{
				memset(buf, 0, BUF_SIZE);
				int ret = recv(socketfd, buf, BUF_SIZE-1, 0);
				if(ret < 0)
				{
					if((errno == EAGAIN) ||(errno == EWOULDBLOCK))
					{
						printf("read later \n");
						break;
					}
					close(socketfd);
					break;
				}
				else if(ret == 0)
				{
					close(socketfd);
				}
				else
				{
					printf("get %d bytes of content: %s \n", ret, buf);
					memset(buf, 0, BUF_SIZE);
					sprintf(buf, "Server gets %d bytes", ret);
				}
			}
		}
		else
		{
			printf("something else is happened \n");
		}
	}
}

int main(int argc, char* argv[ ])
{
	
	const char* ser_ip = NULL;
	int ser_port;
	int ret = 0;
	
	if(argc == 2)
	{
		ser_port = atoi(argv[2]);
		ser_ip = argv[1];
	}
	else
	{
		ser_port = 1234;
		ser_ip = "192.168.65.150";
	}
	printf("ip_address:%s  port:%d \n", ser_ip, ser_port);

	struct sockaddr_in address;
	bzero(&address, sizeof(address));
	address.sin_family = AF_INET;
	address.sin_port = htons(ser_port);
	inet_pton(AF_INET, ser_ip, &address.sin_addr);

	int listenfd = socket(PF_INET, SOCK_STREAM, 0);
	assert(listenfd >= 0);

	ret = bind(listenfd, (struct sockaddr*)&address, sizeof(address));
	assert(ret != -1);

	ret = listen(listenfd, 5);
	assert(listenfd != -1);

	struct epoll_event events[MAX_EVENT_NUMBER];
	int epollfd = epoll_create(5);
	assert(epollfd != -1);
	addfd(epollfd,  listenfd, true);

	while(1)
	{
		int ret = epoll_wait(epollfd, events, MAX_EVENT_NUMBER, -1);
		if(ret < 0)
		{
			printf("epoll failure \n");
			break;
		}

		lt(events, ret, epollfd, listenfd);
		//et(events, ret, epollfd, listenfd);
	}

	close(listenfd);

	return 0;
}
