package Windows;

import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

public class Window implements ActionListener {

    private JPanel appPanel = new JPanel();

    private void initWindow() {
        JFrame f = new JFrame();// creating instance of JFrame

        // creates Jpanel with the layout manager Spring Layout
        SpringLayout spring = new SpringLayout();
        JPanel menuPanel = new JPanel(spring);
        menuPanel.setBackground(Color.red);// set color to red for debugging

        appPanel.setBackground(Color.blue);// set color to blue for debugging

        JButton button1 = new JButton("Name");// creating instance of JButton
        button1.addActionListener(this);
        // button1.setBounds(130, 100, 100, 40);// x axis, y axis, width, height
        menuPanel.add(button1);// adding button in JFrame

        JButton button2 = new JButton("Add Calc");// creating instance of JButton
        // button2.setBounds(130, 150, 100, 40);// x axis, y axis, width, height
        menuPanel.add(button2);// adding button in JFrame

        JButton button3 = new JButton("Cars");// creating instance of JButton
        // button3.setBounds(130, 200, 100, 40);// x axis, y axis, width, height
        menuPanel.add(button3);// adding button in JFrame

        f.setTitle("Window1 Test");

        // contraints set for buttons to be 10px part from top to bottom of
        // containers
        spring.putConstraint(
                SpringLayout.NORTH, button1, 10,
                SpringLayout.SOUTH, button2);

        spring.putConstraint(
                SpringLayout.NORTH, button2, 10,
                SpringLayout.SOUTH, button3);

        GridLayout grid = new GridLayout(1, 2);
        f.setSize(400, 500);// 400 width and 500 height
        f.setLayout(grid);
        grid.addLayoutComponent(null, menuPanel);
        f.setVisible(true);// making the frame visible
        // adds panels to Jframe
        f.add(menuPanel);
        f.add(appPanel);
    }

    private void optionName() {

    }

    public static void main(String[] args) {
        Window window = new Window();
        window.initWindow();
    }

    @Override
    public void actionPerformed(ActionEvent arg0) {

        appPanel.setVisible(false);
    }

}