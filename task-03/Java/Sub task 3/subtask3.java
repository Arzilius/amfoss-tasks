import java.util.Scanner;

public class subtask3 {

    public static void printDiamond(int n) {
        if (n < 1) {
            System.out.println("Number should be greater than 1");
            return;
        }

        // Calculate the middle point
        int mid = n / 2;

        // Upper part of the diamond
        for (int i = 1; i <= n; i += 2) {
            // Calculate and print leading spaces
            int spaces = mid - i / 2;
            System.out.print(" ".repeat(spaces));

            // Print stars
            System.out.println("*".repeat(i));
        }

        // Lower part of the diamond
        if (n % 2 == 0) {
            for (int i = n - 1; i >= 1; i -= 2) {
                // Calculate and print leading spaces with a slight shift for asymmetry
                int spaces = mid - i / 2 + 1;  // Slightly shift the spaces to the right
                System.out.print(" ".repeat(spaces - 1));  // Reduce one space for left shift

                // Print stars
                System.out.println("*".repeat(i));
            }
        } else {
            for (int i = n - 2; i >= 1; i -= 2) {
                // Calculate and print leading spaces
                int spaces = mid - i / 2;
                System.out.print(" ".repeat(spaces));

                // Print stars
                System.out.println("*".repeat(i));
            }
        }
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Enter the number of rows for the diamond: ");
        int n = scanner.nextInt();

        printDiamond(n);
    }
}

