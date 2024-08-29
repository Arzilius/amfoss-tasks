defmodule FileCopy do
  def copy_content do
    input_filename = "input.txt"
    output_filename = "output.txt"

    case File.read(input_filename) do
      {:ok, content} ->
        case File.write(output_filename, content) do
          :ok -> IO.puts("Content successfully written to #{output_filename}")
          {:error, reason} -> IO.puts("Error writing to file: #{reason}")
        end

      {:error, reason} ->
        IO.puts("Error reading file: #{reason}")
    end
  end
end

FileCopy.copy_content()

