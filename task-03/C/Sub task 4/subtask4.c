#include <stdio.h>
#include <stdlib.h>

void print_diamond(FILE *output, int n) {
    if (n < 1) {
        fprintf(output, "Number should be greater than 1\n");
        return;
    }

    int mid = n / 2;

    // Upper part of the diamond
    for (int i = 1; i <= n; i += 2) {
        int spaces = mid - i / 2;
        for (int j = 0; j < spaces; ++j) {
            fprintf(output, " ");
        }
        for (int j = 0; j < i; ++j) {
            fprintf(output, "*");
        }
        fprintf(output, "\n");
    }

    // Lower part of the diamond
    if (n % 2 == 0) {
        for (int i = n - 1; i >= 1; i -= 2) {
            int spaces = mid - i / 2 + 1;
            for (int j = 0; j < spaces - 1; ++j) {
                fprintf(output, " ");
            }
            for (int j = 0; j < i; ++j) {
                fprintf(output, "*");
            }
            fprintf(output, "\n");
        }
    } else {
        for (int i = n - 2; i >= 1; i -= 2) {
            int spaces = mid - i / 2;
            for (int j = 0; j < spaces; ++j) {
                fprintf(output, " ");
            }
            for (int j = 0; j < i; ++j) {
                fprintf(output, "*");
            }
            fprintf(output, "\n");
        }
    }
}

int main() {
    int n;
    FILE *input = fopen("input.txt", "r");
    if (input == NULL) {
        perror("Failed to open input.txt");
        return 1;
    }

    FILE *output = fopen("output.txt", "w");
    if (output == NULL) {
        perror("Failed to open output.txt");
        fclose(input);
        return 1;
    }

    fscanf(input, "%d", &n);
    fclose(input);

    print_diamond(output, n);
    fclose(output);
    
printf("file transfer was successful\n");
    return 0;
}

