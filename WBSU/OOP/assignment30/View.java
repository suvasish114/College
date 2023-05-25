import java.applet.*;
import java.awt.*;

public class View extends Applet{
	public void paint(Graphics g){
		g.setColor(new Color(15,20,75));
		g.fillRect(100,100,200,100);
	
		// moon
		g.setColor(new Color(247,249,219));
		g.fillOval(240,120,40,40);
		g.setColor(new Color(15,20,75));
		g.fillOval(240,120,30,30);
		
		// stars
		g.setColor(new Color(247,249,219));
		g.fillOval(134,167,5,5);
		g.fillOval(174,147,3,3);
	}
}
