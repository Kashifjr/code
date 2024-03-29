import java.util.Scanner;
/*
 * Test prgram to regain my bearings on coding in Java. 
 * 3/29/2024
 *  
 */

public class testcode1 {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        String firstName = "";
        String lastName = "";

        System.out.print("What is your FIRST name?: ");
        firstName = scan.nextLine();
        System.out.print("What is your LAST name?: ");
        lastName = scan.nextLine();
        System.out.println();

        System.out.printf("Your name is: " + firstName + " " + lastName + "\n");
        scan.close();
    }
}
