#include <iostream>

void printDiamond(int n) {
    int i, j;

    // Upper part of the diamond
    for (i = 1; i <= n; i += 2) {
        // Print leading spaces
        for (j = (n - i) / 2; j > 0; j--) {
            std::cout << " ";
        }
        // Print stars
        for (j = 0; j < i; j++) {
            std::cout << "*";
        }
        std::cout << std::endl;
    }

    // Lower part of the diamond
    for (i = n - 2; i >= 1; i -= 2) {
        // Print leading spaces
        for (j = (n - i) / 2; j > 0; j--) {
            std::cout << " ";
        }
        // Print stars
        for (j = 0; j < i; j++) {
            std::cout << "*";
        }
        std::cout << std::endl;
    }
}

int main() {
    int n;

    std::cout << "Enter the number of rows for the diamond: ";
    std::cin >> n;

    if (n < 1) {
        std::cout << "Number should be greater than 1\n";
        return 1;
    }

    printDiamond(n);

    return 0;
}

