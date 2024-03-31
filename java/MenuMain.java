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
             * Volume of a cube is v=s^3. The length, width and height are all 
             * equal, therefore only one side is n
             *   eeded to solve the equation.
             */
            switch (input){
                case "":
                    System.out.println("No input detected. Try again!");;
                    break;
                case "1":   
                    cube cube = new cube();
                    System.out.print("Cube Calculator\n"+line2+"\n"+"Enter a number: ");
                    double side = scan.nextDouble();
                    double volume = cube.cubeVolume(side);
                    System.out.println("\nThe volume of the cube is: "+volume+"^m3");
                    input = "";
                    break;

                default:
                    System.out.println("invalid input. Try Again!");
            }//end of switch 
        }
        scan.close();
    }
}
