#define _GNU_SOURCE 	//to use POLLRDHUP 


#include <stdio.h>
#include <strings.h>
#include <string.h>
#include <sys/types.h>
#include <sys/socket.h>
#include <arpa/inet.h>
#include <assert.h>
#include <poll.h>
#include <unistd.h>
#include <fcntl.h>
#include <stdlib.h>


#define BUFFER_SIZE 64


int main(int argc, char *argv[])
{
	const char *ser_ip = NULL;
	int port;
	
	if(argc < 3)
	{
		ser_ip = "192.168.65.50";
		port = 1234;
	}
	else
	{
		ser_ip = argv[1];
		port = atoi(argv[2]);
	}
	printf("Connect to %s:%d \n", ser_ip, port);

	int sockfd;
	struct sockaddr_in ser_address;
	
	bzero(&ser_address, sizeof(ser_address));
	ser_address.sin_family = AF_INET;
	ser_address.sin_port = htons(port);
	inet_pton(AF_INET, ser_ip, &ser_address.sin_addr);

	sockfd = socket(PF_INET, SOCK_STREAM, 0);
	assert(sockfd > 0);
	if(connect(sockfd, (struct sockaddr*)&ser_address, sizeof(ser_address)) < 0)
	{
		printf("Connect error \n");
		close(sockfd);
		return -1;
	}

	struct pollfd fds[2];
	fds[0].fd = 0;
	fds[0].events = POLLIN;
	fds[0].revents = 0;
	fds[1].fd = sockfd;
#ifdef _GNU_SOURCE
	fds[1].events = POLLIN | POLLRDHUP;
#else
	fds[1].events = POLLIN;
#endif
	fds[1].revents = 0;

	char buf[BUFFER_SIZE];
	int pipefd[2];
	int ret = pipe(pipefd);
	assert(ret != -1);

	while(1)
	{
		ret = poll(fds, 2, -1);
		if(ret < 0)
		{
			printf("poll failure \n");
			break;
		}
#ifdef _GNU_SOURCE
		if(fds[1].revents & POLLRDHUP)
		{
			printf("server close the connect \n");
			break;
		}
#endif
		else if(fds[1].revents & POLLIN)
		{
			memset(buf, '\0', sizeof(buf));
			ret = recv(sockfd, buf, BUFFER_SIZE-1, 0);
			if(ret == 0)
			{
				printf("server close the connect \n");
				break;
			}
			printf("%s \n", buf);
		}

		if(fds[0].revents & POLLIN)
		{
			/*
			ret = splice(0, NULL, pipefd[1], NULL, 32768,
				SPLICE_F_MORE | SPLICE_F_MOVE);
			ret = splice(pipefd[0], NULL, sockfd, NULL, 32768,
				SPLICE_F_MORE | SPLICE_F_MOVE);
				*/
		}
	}
	
	close(sockfd);
	return 0;
	
}
