#include <iostream>
#include <fstream>
#include <string>

void print_diamond(std::ofstream &output, int n) {
    if (n < 1) {
        output << "Number should be greater than 1\n";
        return;
    }

    int mid = n / 2;

    // Upper part of the diamond
    for (int i = 1; i <= n; i += 2) {
        int spaces = mid - i / 2;
        output << std::string(spaces, ' ') << std::string(i, '*') << "\n";
    }

    // Lower part of the diamond
    if (n % 2 == 0) {
        for (int i = n - 1; i >= 1; i -= 2) {
            int spaces = mid - i / 2 + 1;
            output << std::string(spaces - 1, ' ') << std::string(i, '*') << "\n";
        }
    } else {
        for (int i = n - 2; i >= 1; i -= 2) {
            int spaces = mid - i / 2;
            output << std::string(spaces, ' ') << std::string(i, '*') << "\n";
        }
    }
}

int main() {
    int n;
    std::ifstream input("input.txt");
    if (!input) {
        std::cerr << "Failed to open input.txt\n";
        return 1;
    }

    std::ofstream output("output.txt");
    if (!output) {
        std::cerr << "Failed to open output.txt\n";
        return 1;
    }

    input >> n;
    input.close();

    print_diamond(output, n);
    output.close();
    
    std::cout << "File transfer was successful\n";
    return 0;
}

