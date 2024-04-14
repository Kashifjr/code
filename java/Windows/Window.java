package Windows;

import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

public class Window implements ActionListener {

    // CardLayout card = new CardLayout();
    GridLayout grid;
    // appPanel is a panel that contains the panel of "Cards"
    private JPanel appPanel;
    // Where the components controlled by the CardLayout are initialized:
    // Create the "cards".

    private void initWindow() {
        JFrame f = new JFrame();// creating instance of JFrame

        // create cards
        JPanel Name = new JPanel();
        JPanel Cars = new JPanel();
        JPanel Cube = new JPanel();
        // set each card color
        Name.setBackground(Color.black);
        Cars.setBackground(Color.green);
        Cube.setBackground(Color.yellow);
        // App panel created and Cards are added to App Panel
        appPanel = new JPanel(new CardLayout());
        appPanel.add(Name, "1");
        appPanel.add(Cars, "2");
        appPanel.add(Cube, "3");

        // creates menu Jpanel with the layout manager Spring Layout
        SpringLayout spring = new SpringLayout();
        JPanel menuPanel = new JPanel(spring);
        menuPanel.setBackground(Color.red);// set color to red for debugging

        JButton button1 = new JButton("Name");// creating instance of JButton
        JButton button2 = new JButton("Cube Calc");// creating instance of JButton
        JButton button3 = new JButton("Cars");// creating instance of JButton

        button1.addActionListener(this);
        button2.addActionListener(this);
        button3.addActionListener(this);
        // adding button in JFrame
        menuPanel.add(button1);
        menuPanel.add(button2);
        menuPanel.add(button3);

        button1.setActionCommand("name");
        button2.setActionCommand("cube");
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
    }

    public void actionPerformed(ActionEvent e) {
        CardLayout c1 = (CardLayout) (appPanel.getLayout());
        switch (e.getActionCommand()) {
            case "name":
                c1.show(appPanel, "1");
                System.out.println("NAME OPTION PRESSED");
                break;
            case "cars":
                c1.show(appPanel, "2");
                System.out.println("CARS OPTION PRESSED");
                break;
            case "cube":
                c1.show(appPanel, "3");
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