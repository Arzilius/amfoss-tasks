package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

func printDiamond(output *os.File, n int) {
	if n < 1 {
		fmt.Fprintln(output, "Number should be greater than 1")
		return
	}

	mid := n / 2

	// Upper part of the diamond
	for i := 1; i <= n; i += 2 {
		spaces := mid - i/2
		fmt.Fprintln(output, strings.Repeat(" ", spaces)+strings.Repeat("*", i))
	}

	// Lower part of the diamond
	if n%2 == 0 {
		for i := n - 1; i >= 1; i -= 2 {
			spaces := mid - i/2 + 1
			fmt.Fprintln(output, strings.Repeat(" ", spaces-1)+strings.Repeat("*", i))
		}
	} else {
		for i := n - 2; i >= 1; i -= 2 {
			spaces := mid - i/2
			fmt.Fprintln(output, strings.Repeat(" ", spaces)+strings.Repeat("*", i))
		}
	}
}

func main() {
	inputFile, err := os.Open("input.txt")
	if err != nil {
		fmt.Println("Failed to open input.txt:", err)
		return
	}
	defer inputFile.Close()

	outputFile, err := os.Create("output.txt")
	if err != nil {
		fmt.Println("Failed to open output.txt:", err)
		return
	}
	defer outputFile.Close()

	scanner := bufio.NewScanner(inputFile)
	if scanner.Scan() {
		n, err := strconv.Atoi(strings.TrimSpace(scanner.Text()))
		if err != nil {
			fmt.Println("Invalid number:", err)
			return
		}
		printDiamond(outputFile, n)
	}

	if err := scanner.Err(); err != nil {
		fmt.Println("Error reading input.txt:", err)
	}
	fmt.Println("File transfer was successful")
}

