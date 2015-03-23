/*************************************************
*                   OOB紧急数据发送实例
*
*OBB标志数据中仅有最后一个数据
*会被当做带外数据接收
**************************************************/

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <arpa/inet.h>
#include <assert.h>
#include <unistd.h>
#include <libgen.h>

int main(int argc, char* argv[])
{
	if(argc < 3)
	{
		printf("Useage: %s ip_adress port_number \n", basename(argv[0]));
		return 1;
	}

	const char *ip = argv[1];
	int port = atoi(argv[2]);

	struct sockaddr_in sever_adress;
	bzero(&sever_adress, sizeof(struct sockaddr_in));
	sever_adress.sin_family = AF_INET;
	inet_pton(AF_INET, ip, &sever_adress.sin_addr);
	sever_adress.sin_port = htons(port);

	int sockfd = socket(PF_INET, SOCK_STREAM, 0);
	assert(sockfd > 0);

	if(connect(sockfd, (struct sockaddr*)&sever_adress, sizeof(sever_adress) ) < 0 )
	{
		perror("connection failed\n");
	}
	else
	{
		const char* oob_data = "abc";
		const char* normal_data = "123";
		send(sockfd, normal_data, strlen(normal_data), 0 );
		send(sockfd, oob_data, strlen(oob_data), MSG_OOB); //send OOB data
		send(sockfd, normal_data, strlen(normal_data), 0 );		
	}

	close(sockfd);
	return 0;
}
