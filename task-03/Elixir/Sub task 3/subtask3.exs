defmodule Diamond do
  def print_diamond(n) when n < 1 do
    IO.puts("Number should be greater than 1")
  end

  def print_diamond(n) do
    mid = div(n, 2)

    # Upper part of the diamond
    for i <- 1..n//2 + 1, rem(2 * i - 1, 2) == 1 do
      spaces = mid - i + 1
      stars = 2 * i - 1
      IO.puts String.duplicate(" ", spaces) <> String.duplicate("*", stars)
    end

    # Lower part of the diamond
    if rem(n, 2) == 0 do
      for i <- n//2..1, rem(2 * i - 1, 2) == 1 do
        spaces = mid - i + 1
        stars = 2 * i - 1
        IO.puts String.duplicate(" ", spaces) <> String.duplicate("*", stars)
      end
    else
      for i <- n//2..1, rem(2 * i - 1, 2) == 1 do
        spaces = mid - i + 1
        stars = 2 * i - 1
        IO.puts String.duplicate(" ", spaces) <> String.duplicate("*", stars)
      end
    end
  end
end

IO.write("Enter the number of rows for the diamond: ")
n = IO.gets("") |> String.trim() |> String.to_integer()
Diamond.print_diamond(n)


