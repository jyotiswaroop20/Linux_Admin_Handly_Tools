#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(int argc, char *argv[]) {

    if (argc < 2) {
        printf("Usage: lip <package-name>\n");
        return 1;
    }

    if (strcmp(argv[1], "--help") == 0) {
        printf("LIP - Linux Patch Impact Predictor\n");
        printf("Usage: lip <package-name>\n");
        return 0;
    }

    char cmd[512];

    snprintf(cmd, sizeof(cmd),
             "python3 /usr/local/lib/lip/predictor.py %s",
             argv[1]);

    system(cmd);
    return 0;
}

