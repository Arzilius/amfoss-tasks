package main

import (
	"fmt"
	"strings"
)

func printDiamond(n int) {
	if n < 1 {
		fmt.Println("Number should be greater than 1")
		return
	}

	// Calculate the middle point
	mid := n / 2

	// Upper part of the diamond
	for i := 1; i <= n; i += 2 {
		// Calculate and print leading spaces
		spaces := mid - i/2
		fmt.Print(strings.Repeat(" ", spaces))

		// Print stars
		fmt.Println(strings.Repeat("*", i))
	}

	// Lower part of the diamond
	if n%2 == 0 {
		for i := n - 1; i >= 1; i -= 2 {
			// Calculate and print leading spaces
			spaces := mid - i/2 + 1 // Slightly adjust spaces for asymmetry
			fmt.Print(strings.Repeat(" ", spaces))

			// Print stars
			fmt.Println(strings.Repeat("*", i))
		}
	} else {
		for i := n - 2; i >= 1; i -= 2 {
			// Calculate and print leading spaces
			spaces := mid - i/2
			fmt.Print(strings.Repeat(" ", spaces))

			// Print stars
			fmt.Println(strings.Repeat("*", i))
		}
	}
}

func main() {
	var n int
	fmt.Print("Enter the number of rows for the diamond: ")
	_, err := fmt.Scan(&n)
	if err != nil {
		fmt.Println("Invalid input")
		return
	}

	printDiamond(n)
}

