def print_diamond(n):
    if n < 1:
        return "Number should be greater than 1\n"

    result = []
    mid = n // 2

    # Upper part of the diamond
    for i in range(1, n + 1, 2):
        spaces = mid - i // 2
        result.append(' ' * spaces + '*' * i)
    
    # Lower part of the diamond
    if n % 2 == 0:
        for i in range(n - 1, 0, -2):
            spaces = mid - i // 2 + 1
            result.append(' ' * (spaces - 1) + '*' * i)
    else:
        for i in range(n - 2, 0, -2):
            spaces = mid - i // 2
            result.append(' ' * spaces + '*' * i)
    
    return '\n'.join(result) + '\n'

def main():
    try:
        with open('input.txt', 'r') as infile:
            n = int(infile.read().strip())
        
        diamond = print_diamond(n)
        
        with open('output.txt', 'w') as outfile:
            outfile.write(diamond)
        
        print("File transfer was successful")

    except FileNotFoundError:
        print("Failed to open input.txt")
    except ValueError:
        print("Invalid number in input.txt")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()

