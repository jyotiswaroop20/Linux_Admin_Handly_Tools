#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(int argc, char *argv[]) {

    if (argc > 1 && strcmp(argv[1], "--help") == 0) {
        printf("LSAD - Linux System Aging Detector\n");
        printf("Usage: lsad\n");
        return 0;
    }

    system("python3 /usr/local/lib/lsad/analyzer.py");
    return 0;
}

