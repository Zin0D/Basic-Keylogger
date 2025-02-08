#include <winsock2.h>
#include <stdio.h>
#include <stdlib.h>
//Return 0 = no failure, ASM like.
//Return 1 = Failure.
//https://learn.microsoft.com/en-us/windows/win32/api/winsock2/ Documentation.
//Or use Exit.

#pragma comment(lib,"ws2_32.lib")

int main(int argc, char *argv[]) {
    printf("Creating WinSocket..."); //Sugoma Balls fucking Windows
    
    WSADATA data; //Holds Information about WinSockLib
    SOCKET sock;
    SOCKET check_sock_invalid = INVALID_SOCKET;
    struct sockaddr_in addr;

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
    addr.sin_addr.s_addr = inet_addr("127.0.0.1");
    addr.sin_port = htons(80);

    if (bind(sock, (SOCKADDR*) &addr, sizeof(addr)) == SOCKET_ERROR){
        printf("Failed to create socket with IP\n");
        exit(1);
    }

    return 0;
    exit(0);
}