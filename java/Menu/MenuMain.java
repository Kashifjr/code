package Menu;

import java.util.Scanner;
import java.util.stream.Stream;
import java.io.*;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;

/*
 * TODO: EXCEPTION HANDLING!!
 */
public class MenuMain {
    public static void main(String[] args) throws IOException {
        String input = "";
        Scanner scan = new Scanner(System.in);
        String topLine = "=================================";
        String line2 = "---------------------------------";
        String fileFolder = "/home/shika/code/java/Menu/files/";
        String options = """
                Cube Volume Calc.......1
                File Writer............2fileFolder
                    """;

        while (!input.equals("q")) {
            System.out.println(topLine + "\n" + "Menu" + "\n" + line2 + "\n" + options);
            input = scan.next();

            /*
             * Volume of a cube is v=s^3. The length, width and height are all
             * equal, therefore only one side is
             * needed to solve the equation.
             */
            switch (input) {
                case "q":
                    System.out.println(line2 + "\nThanks for using the Program!\n" + topLine);
                    break;
                case "1":
                    cube cube = new cube();
                    System.out.print("Cube Calculator\n" + line2 + "\n" + "Enter a number: ");
                    double side = scan.nextDouble();
                    double volume = cube.cubeVolume(side);
                    System.out.println("\nThe volume of the cube is: " + volume + "^m3");
                    input = "";
                    break;
                case "2": {
                    System.out.print("File writer\n" + line2 + "\n"
                            + "To edit existing file or create new file, enter file name: ");
                    String seeking = scan.next();
                    File file = new File(fileFolder.concat(seeking));
                    try {
                        if (file.exists()) {
                            FileWriter fileWriter = new FileWriter(file);
                            System.out.println("Enter text to input:");
                            String textToFile = scan.nextLine();
                            System.out.println(textToFile);
                            fileWriter.write(textToFile);
                            fileWriter.close();
                            System.out.println(file.getName() + "Text has been written and saved!");
                        } else {
                            file.createNewFile();
                            FileWriter fileWriter = new FileWriter(file);
                            System.out.println(file.getName() + " has been created. Enter text to input:");
                            String textToFile = scan.nextLine();
                            fileWriter.write(textToFile);
                            fileWriter.close();
                            System.out.println(file.getName() + "Text has been written and saved!");
                        }
                    } catch (Exception e) {
                        System.out.println("An error occurred.");
                        e.printStackTrace();
                    }
                    break;
                }
                case "3": {
                    System.out.print("File Reader\n" + line2 + "\n" + "Enter an existing file: ");
                    String seeking = scan.next();
                    File file = new File(fileFolder.concat(seeking));
                    try {
                        Scanner reader = new Scanner(file);
                        while (reader.hasNextLine()) {
                            String data = reader.nextLine();
                            System.out.println(data);
                        }
                        reader.close();
                    } catch (FileNotFoundException e) {
                        System.out.println("File cannot be found");
                    }

                    break;
                }
                case "4": {
                    System.out.println("Delete File\n" + line2 + "\n" + "Enter existing file to delete: ");
                    String seeking = scan.next();
                    File file = new File(fileFolder.concat(seeking));
                    if (file.exists()) {
                        file.delete();
                        System.out.println(seeking + " has been deleted.");
                    } else
                        System.out.println("No file of that name exists.");

                    break;
                }

                case "5": {
                    System.out.println(
                            "Show Files\n" + line2 + "\n" + "There are x files in the directory " + fileFolder);
                    // File f = new File("/home/shika/code/java/Menu/files");
                    // File[] fileList = f.listFiles();
                }
                default:
                    System.out.println("invalid input. Try Again!");
            }// end of switch
        }
        scan.close();
    }
}