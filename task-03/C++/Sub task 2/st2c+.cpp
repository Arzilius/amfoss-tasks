#include <iostream>
#include <fstream>
#include <string>

int main() {
    std::ifstream inputFile("input.txt");  // Open input file for reading
    std::ofstream outputFile("output.txt"); // Open output file for writing

    if (!inputFile) {
        std::cerr << "Error opening input file" << std::endl;
        return 1;
    }

    if (!outputFile) {
        std::cerr << "Error opening output file" << std::endl;
        return 1;
    }

    std::string line;
    while (std::getline(inputFile, line)) {
        outputFile << line << std::endl;  // Write the line to the output file
    }

    std::cout << "File copy completed." << std::endl;

    // Files are automatically closed when the file streams go out of scope
    return 0;
}
