def print_diamond(n)
  if n < 1
    return "Number should be greater than 1\n"
  end

  result = []
  mid = n / 2

  # Upper part of the diamond
  (1..n).step(2) do |i|
    spaces = mid - i / 2
    result << ' ' * spaces + '*' * i
  end

  # Lower part of the diamond
  if n.even?
    (n - 1).step(1, -2) do |i|
      spaces = mid - i / 2 + 1
      result << ' ' * (spaces - 1) + '*' * i
    end
  else
    (n - 2).step(1, -2) do |i|
      spaces = mid - i / 2
      result << ' ' * spaces + '*' * i
    end
  end

  result.join("\n") + "\n"
end

def main
  begin
    input = File.read('input.txt').strip
    n = input.to_i

    diamond = print_diamond(n)

    File.write('output.txt', diamond)

    puts "File transfer was successful"
  rescue Errno::ENOENT
    puts "Failed to open input.txt"
  rescue ArgumentError
    puts "Invalid number in input.txt"
  rescue => e
    puts "An error occurred: #{e.message}"
  end
end

main

