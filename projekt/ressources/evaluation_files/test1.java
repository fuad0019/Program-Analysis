import java.util.Scanner;

public class SimpleJavaProgram {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.println("Enter something: ");
        String userInput = scanner.nextLine();

        String response = processInput(userInput);

        System.out.println("Response: " + response);
    }

    private static String processInput(String input) {
        // Perform some processing on the input and return a response
        return "You entered: " + input;
    }
}
