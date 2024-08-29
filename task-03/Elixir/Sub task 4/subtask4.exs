defmodule Diamond do
  def print_diamond(output_file, n) when n < 1 do
    IO.write(output_file, "Number should be greater than 1\n")
  end

  def print_diamond(output_file, n) do
    mid = div(n, 2)

    # Upper part of the diamond
    for i <- Enum.map(1..div(n, 2) + 1, &(&1 * 2 - 1)) do
      spaces = mid - div(i, 2)
      IO.write(output_file, String.duplicate(" ", spaces) <> String.duplicate("*", i) <> "\n")
    end

    # Lower part of the diamond
    lower_part =
      if rem(n, 2) == 0 do
        Enum.map(Enum.reverse(1..div(n, 2)), &(&1 * 2 - 1))
      else
        Enum.map(Enum.reverse(1..div(n - 1, 2)), &(&1 * 2 - 1))
      end

    for i <- lower_part do
      spaces = mid - div(i, 2)
      IO.write(output_file, String.duplicate(" ", spaces) <> String.duplicate("*", i) <> "\n")
    end
  end

  def main do
    case File.read("input.txt") do
      {:ok, content} ->
        n = String.trim(content) |> String.to_integer()

        File.open("output.txt", [:write], fn output_file ->
          print_diamond(output_file, n)
        end)

        IO.puts("File transfer was successful")

      {:error, reason} ->
        IO.puts("Failed to open input.txt: #{reason}")
    end
  end
end

Diamond.main()

