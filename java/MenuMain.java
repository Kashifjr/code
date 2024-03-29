import java.util.Scanner;


public class MenuMain {
    public static void main(String[] args) {
        String input = "";
        Scanner scan = new Scanner(System.in);
        String topLine = "=================================";
        String line2 = "---------------------------------";
        String options = "Cube Volume Calc.......1\n";

        while(input != "q"){
            System.out.println(topLine+"\n"+"Menu"+"\n"+line2+"\n"+options);
            input = scan.nextLine();
            
            /*
             * Volume of a cube is v=s^3. The lenght, width and height are all 
             * equal, therefore only one side is needed to solve the equation.
             * 
             * TODO: create and import new class called Cube Volume and use this 
             * class to calculate/return value of a cube's volume.
             */
            switch (input){
                case "1":
                    
                    int num;
                    System.out.print("Cube Calculator\n"+line2+"\n"+"Enter a number: ");
                    num = scan.nextInt();

                    //import math and use exp to do this properly..
                    double v = num * num * num;

                    System.out.println("\nThe volume of the cube is: "+v+"^m3"+line2);

                    break;
                default:
                    System.out.println("invalid input. Try Again!");
            }
            
        }
        scan.close();
    }
}
