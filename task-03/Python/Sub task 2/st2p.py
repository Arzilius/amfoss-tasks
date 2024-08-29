# Open the input file in read mode
with open("input.txt", "r") as input_file:
    # Read the content of the input file
    content = input_file.read()

# Open the output file in write mode
with open("output.txt", "w") as output_file:
    # Write the content to the output file
    output_file.write(content)

print("File copy completed.")

