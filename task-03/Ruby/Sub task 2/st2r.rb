# Read from input.txt
input_filename = 'input.txt'
output_filename = 'output.txt'

begin
  # Open and read the content of input.txt
  input_content = File.read(input_filename)

  # Write the content to output.txt
  File.open(output_filename, 'w') do |file|
    file.write(input_content)
  end

  puts "Content successfully written to #{output_filename}"
rescue Errno::ENOENT
  puts "Error: File not found - #{input_filename}"
rescue => e
  puts "An error occurred: #{e.message}"
end

