#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(int argc, char *argv[])
{
    if (argc < 2)
    {
        printf("Usage: lcmt <snapshot|diff|history>\n");
        return 1;
    }

    char cmd[256];

    snprintf(
        cmd,
        sizeof(cmd),
        "python3 /usr/local/lib/lcmt/tracker.py %s",
        argv[1]
    );

    system(cmd);

    return 0;
}

