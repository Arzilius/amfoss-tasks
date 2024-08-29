import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;

public class subtask2 {
    public static void main(String[] args) {
        String inputFilename = "input.txt";
        String outputFilename = "output.txt";

        try {
            // Read the content of input.txt
            String content = new String(Files.readAllBytes(Paths.get(inputFilename)));

            // Write the content to output.txt
            Files.write(Paths.get(outputFilename), content.getBytes());

            System.out.println("Content successfully written to " + outputFilename);
        } catch (IOException e) {
            System.err.println("An error occurred: " + e.getMessage());
        }
    }
}

