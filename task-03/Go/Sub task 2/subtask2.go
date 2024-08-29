package main

import (
	"fmt"
	"io/ioutil"
)

func main() {
	inputFilename := "input.txt"
	outputFilename := "output.txt"

	// Read the content of input.txt
	content, err := ioutil.ReadFile(inputFilename)
	if err != nil {
		fmt.Println("Error reading file:", err)
		return
	}

	// Write the content to output.txt
	err = ioutil.WriteFile(outputFilename, content, 0644)
	if err != nil {
		fmt.Println("Error writing to file:", err)
		return
	}

	fmt.Println("Content successfully written to", outputFilename)
}

