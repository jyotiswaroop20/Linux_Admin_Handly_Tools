#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>
#include <sys/wait.h>

#define TRACE_LOG "/tmp/lcbp_trace.log"

int main(int argc, char *argv[]) {

    if (argc < 2) {
        printf("Usage: lcbp <command>\n");
        return 1;
    }

    if (strcmp(argv[1], "--help") == 0) {
        printf("LCBP - Linux Command Behavior Profiler\n");
        printf("Usage: lcbp <command>\n");
        return 0;
    }

    pid_t pid = fork();

    if (pid == 0) {
        /* Child: run strace */
        char *args[argc + 5];

        args[0] = "strace";
        args[1] = "-f";
        args[2] = "-o";
        args[3] = TRACE_LOG;

        for (int i = 1; i < argc; i++) {
            args[i + 3] = argv[i];
        }

        args[argc + 3] = NULL;

        execvp("strace", args);
        perror("execvp failed");
        exit(1);
    } 
    else if (pid > 0) {
        /* Parent */
        printf("[LCBP] Profiling command...\n");
        wait(NULL);
        printf("[LCBP] Command execution completed.\n");
        printf("[LCBP] Generating report...\n");
        system("/usr/bin/python3 /usr/local/lib/lcbp/analyzer.py");
    } 
    else {
        perror("fork failed");
        return 1;
    }

    return 0;
}

