#include <stdio.h>
#include <stdlib.h>
#define ON_SUCCESS 0 //Compiler replaces all define statements.
// Hacking by using encrypted define payload to be replaced instead of variables?

// JUST A TESTING GROUND IN WHICH I WILL DO SOME C STUFF.

void swap(int *px, int *py){
    int tmp = *px;
    *px = *py;
    *py = tmp;
    puts("Swaping.....");
}

void stringed(char **chad, char **chad2){
    char *t = *chad;
    *chad = *chad2;
    *chad2 = t;
    printf("Strings swapped.");
}

int main(){
    puts("Hello World");
    printf("%s\n", "Hello World");
    int x = 3;
    int y = 4;
    char *chad = "Hello fortnut";
    char *chad2 = "Hello Chadut";
    printf("Original Values: x: %d, y: %d\n", x,y);
    swap(&x, &y);
    printf("Swaped: x: %d, y: %d",x,y);

    stringed(&chad,&chad2);
    printf("%s, %s", chad, chad2);

    return ON_SUCCESS;
}
