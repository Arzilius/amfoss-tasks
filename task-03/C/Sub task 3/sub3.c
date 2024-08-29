#include <stdio.h>
#include <stdlib.h>

void print_diamond(int n) {
    if (n < 1) {
        printf("Number should be greater than 1\n");
        return;
    }

    int mid = n / 2;

    // Upper part of the diamond
    for (int i = 1; i <= n; i += 2) {
        int spaces = mid - i / 2;
        for (int j = 0; j < spaces; ++j) {
            printf(" ");
        }
        for (int j = 0; j < i; ++j) {
            printf("*");
        }
        printf("\n");
    }

    // Lower part of the diamond
    if (n % 2 == 0) {
        for (int i = n - 1; i >= 1; i -= 2) {
            int spaces = mid - i / 2 + 1;
            for (int j = 0; j < spaces - 1; ++j) {
                printf(" ");
            }
            for (int j = 0; j < i; ++j) {
                printf("*");
            }
            printf("\n");
        }
    } else {
        for (int i = n - 2; i >= 1; i -= 2) {
            int spaces = mid - i / 2;
            for (int j = 0; j < spaces; ++j) {
                printf(" ");
            }
            for (int j = 0; j < i; ++j) {
                printf("*");
            }
            printf("\n");
        }
    }
}

int main() {
    int n;
    printf("Enter the number of rows for the diamond: ");
    scanf("%d", &n);

    print_diamond(n);

    return 0;
}

