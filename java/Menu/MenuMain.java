package Menu;

import java.util.Scanner;
import java.util.Set;
import java.io.*;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.stream.*;

/*
 * TODO: EXCEPTION HANDLING!!
 */
public class MenuMain {
    public static Set<String> listDirectory(String dir) throws IOException {
        try (Stream<Path> stream = Files.list(Paths.get(dir))) {
            return stream
            .filter(file -> !Files.isDirectory(file))
            .map(Path::getFileName)
            .map(Path::toString)
            .collect(Collectors.toSet());
        }
    }

    public static void main(String[] args) throws IOException {
        String input = "";
        Scanner scan = new Scanner(System.in);
        String topLine = "=================================";
        String line2 = "---------------------------------";
        String fileFolder = "/home/shika/code/java/Menu/files/";
        String options = """
                Cube Volume Calc.......1
                File Writer............2
                Read Files.............3
                Delete Files...........4
                Preview Files..........5
                    """;
                
        while (!input.equals("q")) {
            System.out.println(topLine+"\n"+options+"\n"+line2);
            input = scan.nextLine();
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
                }//case2
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
                }//case3
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
                }//case4

                case "5": {
                    Path dir =  Paths.get("/home/shika/code/java/Menu/files");
                    int numOfFiles = dir.getNameCount();
                    System.out.println("Show Files\n" + line2 + "\n" + "There are "+numOfFiles+" files in the directory " + fileFolder+":");
                    try (Stream<Path> paths = Files.walk(dir)) {
                        // print all files and folders
                        paths.forEach(System.out::println);
                    } catch (IOException ex) {
                        ex.printStackTrace();
                    }

                    /*
                     * Files imports .nio
                     * using Files to try and read all of the .txt files in the 
                     * /home/shika/code/java/Menu/files directory. 
                     * 
                     */
                    Path test = Paths.get("/home/shika/code/java/Menu/files");
                    Stream<Path> walker = Files.walk(test);
                    System.out.println("Test1: "+test.getNameCount());
                    walker.filter(Files::isRegularFile)
                    .collect(Collectors.toList())
                    .forEach(System.out::println);

                    walker.toList();
                    walker.close();


                    System.out.println(line2);
                    }

                }//case5
 
            }// end of switch        
            scan.close();
        }
    }
//}