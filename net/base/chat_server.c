#define _GNU_SOURCE


#include <stdio.h>
#include <unistd.h>
#include <string.h>
#include <strings.h>
#include <assert.h>
#include <netinet/in.h>
#include <sys/types.h>
#include <sys/socket.h>
#include <arpa/inet.h>
#include <errno.h>
#include <fcntl.h>
#include <stdlib.h>
#include <poll.h>


#define FD_LIMIT 	65535
#define USER_LIMIT 	5
#define BUFF_SIZE	64


typedef struct client_data
{
	struct sockaddr_in address;
	char *write_buf;
	char buf[BUFF_SIZE];
}client_data;


int setnonblock(int fd)
{
	int old_option = fcntl(fd, F_GETFL);
	int new_option = old_option | O_NONBLOCK;

	fcntl(fd, F_SETFL, new_option);
	return old_option;
}

int main(int argc, char *argv[])
{
	const char *ip_ser = NULL;
	int port_ser;

	if(argc < 3)
	{
		ip_ser = "192.168.65.50";
		port_ser = 1234;
	}
	else
	{
		ip_ser = argv[1];
		port_ser = atoi(argv[2]);
	}
	printf("Server: %s:%d \n", ip_ser, port_ser);

	int listenfd_ser;
	struct sockaddr_in address_ser;
	int ret;

	bzero(&address_ser, sizeof(address_ser));
	address_ser.sin_family= AF_INET;
	address_ser.sin_port = htons(port_ser);
	inet_pton(AF_INET, ip_ser, &address_ser.sin_addr);

	listenfd_ser = socket(PF_INET, SOCK_STREAM, 0);
	assert(listenfd_ser >= 0);

	ret = bind(listenfd_ser, (struct sockaddr*)&address_ser, sizeof(address_ser));
	assert(ret != -1);

	ret = listen(listenfd_ser, 5);
	assert(ret != -1);

	client_data* users = (client_data*)malloc(sizeof(client_data)*FD_LIMIT);
	struct pollfd fds[USER_LIMIT + 1];
	int user_counter = 0;

	for(int i = 1; i <= USER_LIMIT; i++)
	{
		fds[i].fd = -1;
		fds[i].events = 0;
		fds[i].revents= 0;
	}
	fds[0].fd = listenfd_ser;
	fds[0].events= POLLIN | POLLERR;
	fds[0].revents = 0;

	while(1)
	{
		ret = poll(fds, user_counter+1, -1);
		if(ret < 0)
		{
			printf("poll failure \n");
			break;
		}

		for(int i = 0; i < user_counter+1; i++)
		{
			if((fds[i].fd == listenfd_ser) && (fds[i].revents & POLLIN))
			{
				struct sockaddr_in client_address;
				socklen_t client_addrlength = sizeof(client_address);
				int connfd = accept(listenfd_ser, (struct sockaddr*)&client_address, &client_addrlength);

				if(connfd < 0)
				{
					printf("errno is %d \n", errno);
					continue;
				}

				//请求太多时关闭新到的连接
				if(user_counter >= USER_LIMIT)
				{
					const char* info = "Too many users \n";
					printf("%s", info);

					send(connfd, info, strlen(info), 0);
					close(connfd);
					continue;
				}

				//对于新到的连接，同时修改fds和users数组
				user_counter++;
				users[connfd].address = client_address;
				setnonblock(connfd);
				fds[user_counter].fd = connfd;
#ifdef _GNU_SOURCE
				fds[user_counter].events = POLLIN | POLLERR | POLLRDHUP;
#else
				fds[user_counter].events = POLLIN | POLLERR;
#endif
				fds[user_counter].revents = 0;
				printf("Comes a new user, now have %d user \n", user_counter);
			}
			else if(fds[i].revents & POLLERR)
			{
				printf("Get an error from %d \n", fds[i].fd);
				char errors[100];
				memset(errors, '\0', 100);
				socklen_t length = sizeof(errors);
				if(getsockopt(fds[i].fd, SOL_SOCKET, SO_ERROR, errors, &length) < 0);
				{
					printf("Get socket option failed \n");
				}
				continue;
			}
#ifdef _GNU_SOURCE		
			else if(fds[i].revents & POLLRDHUP)
			{
				users[fds[i].fd] = users[fds[user_counter].fd];
				close(fds[i].fd);
				fds[i] = fds[user_counter];
				
				i--;
				user_counter--;
				printf("A client left \n");
			}
#endif
			else if(fds[i].revents & POLLIN)
			{
				int connfd = fds[i].fd;
				memset(users[connfd].buf, '\0', 100);
				ret = recv(connfd, users[connfd].buf, BUFF_SIZE-1, 0);
				printf("Get %d bytes of client data: %s  \nfrom %d \n", ret, users[connfd].buf, connfd);

				if(ret < 0)
				{
					//读写出错时关闭连接
					if(errno != EAGAIN)
					{
						close(connfd);
						users[fds[i].fd] = users[fds[user_counter].fd];
						fds[i] = fds[user_counter];
						i--;
						user_counter--;
					}
				}
				else if(ret == 0)
				{		
					users[fds[i].fd] = users[fds[user_counter].fd];
					close(fds[i].fd);
					fds[i] = fds[user_counter];
					
					i--;
					user_counter--;
					printf("A client left \n");

				}
				else //收到数据，通知其他socket 准备接收
				{
					for(int j = 0; j <= user_counter; ++j)
					{
						if(fds[j].fd == connfd)
						{
							continue;
						}

						fds[j].events &= ~POLLIN;
						fds[j].events |= POLLOUT;
						users[fds[j].fd].write_buf = users[connfd].buf;
					}
				}
			}
			else if(fds[i].revents & POLLOUT)
			{
				int connfd = fds[i].fd;
				if(!users[connfd].write_buf)
				{
					continue;
				}
				ret = send(connfd, users[connfd].write_buf, strlen(users[connfd].write_buf), 0);
				
				fds[i].events &= ~POLLOUT;
				
				fds[i].events |= POLLIN;
			}
		}
	}

	free(users);
	close(listenfd_ser);
	return 0;
}
