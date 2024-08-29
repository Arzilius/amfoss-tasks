import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;

public class subtask4 {

    public static void printDiamond(BufferedWriter output, int n) throws IOException {
        if (n < 1) {
            output.write("Number should be greater than 1\n");
            return;
        }

        int mid = n / 2;

        // Upper part of the diamond
        for (int i = 1; i <= n; i += 2) {
            int spaces = mid - i / 2;
            output.write(" ".repeat(spaces) + "*".repeat(i) + "\n");
        }

        // Lower part of the diamond
        if (n % 2 == 0) {
            for (int i = n - 1; i >= 1; i -= 2) {
                int spaces = mid - i / 2 + 1;
                output.write(" ".repeat(spaces - 1) + "*".repeat(i) + "\n");
            }
        } else {
            for (int i = n - 2; i >= 1; i -= 2) {
                int spaces = mid - i / 2;
                output.write(" ".repeat(spaces) + "*".repeat(i) + "\n");
            }
        }
    }

    public static void main(String[] args) {
        try (BufferedReader input = new BufferedReader(new FileReader("input.txt"));
             BufferedWriter output = new BufferedWriter(new FileWriter("output.txt"))) {

            String line = input.readLine();
            if (line != null) {
                int n = Integer.parseInt(line.trim());
                printDiamond(output, n);
                System.out.println("File transfer was successful");
            } else {
                System.out.println("Input file is empty.");
            }

        } catch (IOException e) {
            System.err.println("An error occurred: " + e.getMessage());
        }
    }
}


