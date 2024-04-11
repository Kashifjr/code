package Windows;

import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

public class Window implements ActionListener {

    // CardLayout card = new CardLayout();
    GridLayout grid;
    // appPanel is a panel that contains the panel of "Cards"
    private JPanel appPanel = new JPanel();

    // Where instance variables are declared for cards:
    // final static String BUTTONPANEL = "Card with JButtons";
    // final static String TEXTPANEL = "Card with JTextField";

    // Where the components controlled by the CardLayout are initialized:
    // Create the "cards".
    JPanel Name = new JPanel();
    JPanel Cars = new JPanel();
    JPanel Cube = new JPanel();

    /*
     * TODO//
     * Define and group all layouts with expaination comments
     * 
     */
    private void initWindow() {
        JFrame f = new JFrame();// creating instance of JFrame

        Name.setBackground(Color.black);
        Cars.setBackground(Color.green);
        Cube.setBackground(Color.yellow);

        // Cards are added to App Panel
        appPanel.add("This is the Name option", Name);
        appPanel.add("This is the car option", Cars);
        appPanel.add("This is the cube option", Cube);

        // creates Jpanel with the layout manager Spring Layout
        SpringLayout spring = new SpringLayout();
        JPanel menuPanel = new JPanel(spring);
        menuPanel.setBackground(Color.red);// set color to red for debugging

        // default app panel is BLUE
        appPanel.setBackground(Color.blue);// set color to blue for debugging

        JButton button1 = new JButton("Name");// creating instance of JButton
        button1.addActionListener(this);
        menuPanel.add(button1);// adding button in JFrame
        button1.setActionCommand("name");

        JButton button2 = new JButton("Cube Calc");// creating instance of JButton
        button2.addActionListener(this);
        menuPanel.add(button2);// adding button in JFrame
        button2.setActionCommand("cube");

        JButton button3 = new JButton("Cars");// creating instance of JButton
        button3.addActionListener(this);
        menuPanel.add(button3);// adding button in JFrame
        button3.setActionCommand("cars");

        f.setTitle("Window1 Test");

        // contraints set for buttons to be 10px part from top to bottom of
        // containers
        spring.putConstraint(
                SpringLayout.NORTH, button1, 50,
                SpringLayout.SOUTH, button2);

        spring.putConstraint(
                SpringLayout.NORTH, button2, 50,
                SpringLayout.SOUTH, button3);

        grid = new GridLayout(1, 2);// grid style set 1 row, 2 columns
        f.setSize(400, 500);// 400 width and 500 height
        f.setLayout(grid);
        grid.addLayoutComponent("menuPanel", menuPanel);
        grid.addLayoutComponent("appPanel", appPanel);

        f.setVisible(true);// making the frame visible
        // adds panels to Jframe
        f.add(menuPanel);
        f.add(appPanel);
        Cars.setVisible(false);
        Name.setVisible(false);
        Cube.setVisible(false);
    }

    @Override
    public void actionPerformed(ActionEvent e) {
        switch (e.getActionCommand()) {
            case "name":
                Cars.setVisible(false);
                Name.setVisible(true);
                Cube.setVisible(false);
                System.out.println("NAME OPTION PRESSED");
                break;
            case "cars":
                Cars.setVisible(true);
                Name.setVisible(false);
                Cube.setVisible(false);
                System.out.println("CARS OPTION PRESSED");
            case "cube":
                Cars.setVisible(false);
                Name.setVisible(false);
                Cube.setVisible(true);
                System.out.println("CUBE OPTION PRESSED");
                break;
            default:
                break;
        }

    }

    public static void main(String[] args) {
        Window window = new Window();
        window.initWindow();
    }

}