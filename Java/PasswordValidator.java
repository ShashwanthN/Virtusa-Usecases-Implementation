import java.util.*;

public class PasswordValidator {
    public static void main(String[] args) {
        boolean isValid = false;
        Scanner scanner = new Scanner(System.in);
        while (!isValid) {
            System.out.print("please enter a password:");
            String password = scanner.nextLine();
            isValid = PasswordValidate(password);

            if (isValid) {
                System.out.println("Welcome.");
            } else {
                System.out.println("Password is not strong. Enter again.");
            }
        }
    }static boolean PasswordValidate(String password) {
        boolean passed = true;
        if (password.length() < 8) {
            System.out.println("you are password is missing " + (8 - password.length()) + " characters.");
            passed = false;
        }
        boolean oneUppercase = false;
        boolean oneDigit = false;

        for (int i= 0;i<password.length();i++) {
            char c = password.charAt(i);
            if (Character.isUpperCase(c)) {
                oneUppercase = true;
            }
            if (Character.isDigit(c)) {
                oneDigit = true;
            }
        }
        if (!oneUppercase) {
            System.out.println("add an uppercase letter.");
            passed = false;
        }
        if (!oneDigit) {
            System.out.println("add an digit.");
            passed = false;
        }

        return passed;
    }
}