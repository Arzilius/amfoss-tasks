def print_diamond(n)
  if n < 1
    puts "Number should be greater than 1"
    return
  end

  mid = n / 2

  # Upper part of the diamond
  (1..n).step(2) do |i|
    # Calculate and print leading spaces
    spaces = mid - i / 2
    puts ' ' * spaces + '*' * i
  end

  # Lower part of the diamond
  if n.even?
    (n - 1).step(1, -2) do |i|
      # Calculate and print leading spaces with a slight shift for asymmetry
      spaces = mid - i / 2 + 1
      puts ' ' * (spaces - 1) + '*' * i
    end
  else
    (n - 2).step(1, -2) do |i|
      spaces = mid - i / 2
      puts ' ' * spaces + '*' * i
    end
  end
end

# Example usage
print "Enter the number of rows for the diamond: "
n = gets.to_i
print_diamond(n)

