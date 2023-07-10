import java.awt.*;
import java.awt.event.*;
import javax.swing.*;
import javax.swing.event.*;

class Form{
	Form(){
		JFrame jFrame = new JFrame("Simple Form");
		jFrame.setLayout(new FlowLayout());
		jFrame.setSize(500,500);
		jFrame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
 		
 		// TEXTFIELD
 		jFrame.add(new JLabel("Full Name: "));
 		JTextField jtf = new JTextField(15);
 		jFrame.add(jtf);
 		
 		// CHECKBOX
 		JCheckBox checkBox1 = new JCheckBox("Male");
 		JCheckBox checkBox2 = new JCheckBox("Female");
 		jFrame.add(new JLabel("Gender: "));
 		jFrame.add(checkBox1);
 		jFrame.add(checkBox2);
 		
 		// LIST
 		String subjects[] = {"Bengali","English","Physics","Chemistry","Mathematics"};
 		JList<String> jList = new JList<String>(subjects);
 		jList.setSelectionMode(ListSelectionModel.SINGLE_SELECTION);
 		JScrollPane scroll = new JScrollPane(jList);
 		scroll.setPreferredSize(new Dimension(150,70));
 		jFrame.add(new JLabel("Subject: "));
 		jFrame.add(scroll);
 		
 		JButton button = new JButton("Send");
 		// BUTTON ACTION LISTNER
 		jFrame.add(button);
		jFrame.setVisible(true);
	}
}
class Main{
	public static void main(String args[]){
		SwingUtilities.invokeLater(new Runnable() {
			public void run(){new Form();}
		});
	}
}
