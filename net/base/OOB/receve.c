/*************************************************
*                   OOB紧急数据接收实例
*
*OBB标志数据中仅有最后一个数据
*会被当做带外数据接收
**************************************************/

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <netinet/in.h>
#include <arpa/inet.h>
#include <assert.h>
#include <unistd.h>
#include <errno.h>
#include <libgen.h>

#define BUF_SIZE 1024

int main(int argc, char *argv[])
{
	if(argc < 3)
	{
		printf("Useage: %s ip_adress port_number\n", basename(argv[0]));
		return 1;
	}
	const char *ip_adress = argv[1];
	int port_number = atoi(argv[2]);

	struct sockaddr_in address;
	bzero(&address, sizeof(struct sockaddr_in));
	address.sin_family = AF_INET;
	inet_pton(AF_INET, ip_adress, &address.sin_addr) ;
	address.sin_port = htons(port_number);

	int sockfd = socket(PF_INET, SOCK_STREAM, 0);
	assert(sockfd > 0);

	int ret = bind(sockfd, (struct sockaddr*)&address, sizeof(address));
	assert(ret != -1);

	ret = listen(sockfd, 5);
	assert(-1 != ret);

	struct sockaddr_in client;
	bzero(&client, sizeof(struct sockaddr_in));
	socklen_t client_addrlength = sizeof(client);
	int connfd = accept(sockfd, (struct sockaddr*)&client, &client_addrlength);
	if(connfd < 0)
	{
		printf("error is: %d\n", errno);
	}
	else
	{
		char buf[BUF_SIZE];

		memset(buf, '\0', BUF_SIZE);
		ret = recv(connfd, buf, BUF_SIZE-1, 0);
		printf("got %d bytes of normal data: '%s'\n", ret, buf);

		//receive OOB data
		memset(buf, '\0', BUF_SIZE);
		ret = recv(connfd, buf, BUF_SIZE-1, MSG_OOB);
		printf("got %d bytes of oob data: '%s'\n", ret, buf);

		
		memset(buf, '\0', BUF_SIZE);
		ret = recv(connfd, buf, BUF_SIZE-1, 0);
		printf("got %d bytes of normal data: '%s'\n", ret, buf);

		close(connfd);
	}

	close(sockfd);
	return 0;
}
