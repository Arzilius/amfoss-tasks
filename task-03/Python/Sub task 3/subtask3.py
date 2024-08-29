def print_diamond(n):
    if n < 1:
        print("Number should be greater than 1")
        return

    mid = n // 2

    # Upper part of the diamond
    for i in range(1, n + 1, 2):
        # Calculate and print leading spaces
        spaces = mid - i // 2
        print(" " * spaces + "*" * i)

    # Lower part of the diamond
    if n % 2 == 0:
        for i in range(n - 1, 0, -2):
            # Calculate and print leading spaces with a slight shift for asymmetry
            spaces = mid - i // 2 + 1
            print(" " * (spaces - 1) + "*" * i)
    else:
        for i in range(n - 2, 0, -2):
            spaces = mid - i // 2
            print(" " * spaces + "*" * i)

# Example usage
if __name__ == "__main__":
    n = int(input("Enter the number of rows for the diamond: "))
    print_diamond(n)

