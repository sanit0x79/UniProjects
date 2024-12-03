#include <stdio.h>
#include <netdb.h>
#include <netinet/in.h>
#include <stdlib.h>
#include <string.h>
#include <sys/socket.h>
#include <sys/types.h>
#include <unistd.h> // read(), write(), close()

#define MAX 80
#define PORT 8080
#define SA struct sockaddr

void func(int connfd)
{
    char buff[MAX];
    int n;

    for (;;) // Infinite loop //
        {
            bzero(buff, MAX);
            // read the message from client, copy it into the buffer
            read(connfd, buff, sizeof(buff));
            // print out the buffer content
            printf("From client: %s\t To Client: ", buff);
            // set all the content of the buffer to 0 again
            bzero(buff, MAX);
            n = 0;

            while ((buff[n++] = getchar() != '\n'));

            write(connfd, buff, sizeof(buff));

            if(strncmp("exit", buff, 4) == 0)
            {
                    printf("Server exit...\n");
                    break;
            }
        }
}

int main()
{
    int sockfd, connfd, len;
    struct sockaddr_in servaddr, cli;
    // creating the socket and verifying it
    sockfd = socket(AF_INET, SOCK_STREAM, 0); // AF_INET = IPv4 protocol, SOCK_STREAM = reliable two way connection based byte streams.
    if (sockfd == -1)
    {
        printf("Socket creation failed...\n");
        exit(0);
    }
    else
        printf("Socket successfulyl created..\n");
    bzero(&servaddr, sizeof(servaddr)); // set the entirety of servaddr to 0 using sizeof (memory range), this makes sure that there are no remnants of data left

    servaddr.sin_family = AF_INET;
    servaddr.sin_addr.s_addr = htonl(INADDR_ANY);
    servaddr.sin_port = htons(PORT);

    if ((bind(sockfd, (SA*)&servaddr, sizeof(servaddr)))!= 0)
    {
            printf("Socket bind failed...\n");
            exit(0);
    }
    else
        printf("Socket successfully binded..\n");
    if ((listen(sockfd, 5)) != 0)
    {
            printf("Listen failed...\n");
            exit(0);
    }
    else
        printf("Server listening..\n");
    len = sizeof(cli);

    connfd = accept(sockfd, (SA*)&cli, &len);
    if (connfd < 0)
    {
            printf("Server accept failed...\n");
            exit(0);
    }
    else
        printf("Server accept the client...\n");

    func(connfd);

    close(sockfd);
}
