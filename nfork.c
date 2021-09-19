#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[])
{
    int n = strtol(argv[1], NULL, 10);        
    for(int i = 1; i <= n; i++) {
        if(fork() == 0) {
            printf("PID: %d, Parent PID: %d\n", getpid(), getppid());
            exit(0);
        } else {
           wait(NULL);
        }
    }
    return 0;
}