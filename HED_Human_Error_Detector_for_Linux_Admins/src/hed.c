#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(int argc, char *argv[]) {

    if (argc < 2) {
        printf("Usage: hed <command>\n");
        return 1;
    }

    if (strcmp(argv[1], "--help") == 0) {
        printf("HED - Human Error Detector for Linux Admins\n");
        printf("Usage: hed <command>\n");
        return 0;
    }

    char cmd[2048] = "python3 /usr/local/lib/hed/detector.py ";

    for (int i = 1; i < argc; i++) {
        strcat(cmd, argv[i]);
        strcat(cmd, " ");
    }

    system(cmd);
    return 0;
}
