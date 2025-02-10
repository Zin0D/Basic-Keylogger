#include <winsock2.h>
#include <stdio.h>
#include <stdlib.h>
//Return 0 = no failure, ASM like.
//Return 1 = Failure.
//https://learn.microsoft.com/en-us/windows/win32/api/winsock2/ Documentation.
//Or use Exit.
//https://devdocs.io/c
//Goto for deeply nested code if wanting to jump to another section.

#pragma comment(lib,"ws2_32.lib") //For the Linker.
#define NETWORKING_BUFFER 512
#define ERROR_MESSAGE "HTTP/1.1 404 NOT FOUND"

int main(int argc, char *argv[]) {
    printf("Creating WinSocket..."); //Sugoma Balls fucking Windows
    
    WSADATA data; //Holds Information about WinSockLib
    SOCKET sock;
    SOCKET check_sock_invalid = INVALID_SOCKET;
    struct sockaddr_in addr;
    char buffer[NETWORKING_BUFFER];
    int recv_lenght = NETWORKING_BUFFER;
    char request[] = "GET /index.html HTTP/1.1"; 
    char response[] = " / "; 

    if (WSAStartup(MAKEWORD(2,2),&data) != 0) { //If WsaStartup returns a 0, the Initialisation failed.
        printf("Failed to initialize. : %d\n", WSAGetLastError()); //Backward Compatibility aswell 
        exit(1); //Failed.
    }
    

    if ((sock = socket(AF_INET, SOCK_STREAM, 0)) == check_sock_invalid){
        printf("Invalid Socket Type.\n"); //
        exit(1); //Failed.
    }

    printf("Done :D\n");
    sock = socket(AF_INET, SOCK_STREAM, IPPROTO_TCP); //Returns FD.

    
    
    addr.sin_family = AF_INET;
    addr.sin_addr.s_addr = inet_addr(argv[1]);
    addr.sin_port = htons(80); //Little Endian to Big Endian, (Depending on the System Architecture)

    if (bind(sock, &addr, sizeof(addr)) == SOCKET_ERROR){
        printf("Failed to create socket with IP: %d \n",WSAGetLastError());
        exit(1);
    }

    bind(sock, &addr, sizeof(addr));
    listen(sock, 5);

    if (accept(sock, &addr, 0) == INVALID_SOCKET){
        printf("Connection with Host failed. %d\n", WSAGetLastError());
        exit(1);
    }
    accept(sock, &addr, 0); //Returns da ClientSocket. //The connection is actually made with the socket that is returned by accept.
    
    recv(sock, buffer, recv_lenght, 0); //Updated in Array.
    //Request.
    if (memcmp(buffer, response, strlen(response)) == 0){ //CMP instructions are subtractions of 2 values.
        send(sock, response, strlen(response), 0);
    } else {
        send(sock, ERROR_MESSAGE, strlen(ERROR_MESSAGE), 0); //Send the error message if requested something not in here.
    }

    return 0;

    exit(0);
}