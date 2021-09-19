#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[])
{
    int n = (int) argv[1];        

    for(int i = 1; i < n; i++) {
        if(fork() == 0) {
            printf("Parent PID: %d, PID: %d\n", getpid(), getppid());
            exit(0);
        }
    }
    waitpid();

    return 0;
}