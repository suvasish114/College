import java.awt.*;
import java.applet.*;

public class Circle extends Applet{
	public void paint(Graphics g){
		g.setColor(new Color(156, 39, 176));
		g.drawOval(100,100,200,200);
		g.setColor(new Color(67, 160, 71));
		g.drawOval(120,120,160,160);
		g.setColor(new Color(211, 47, 47));
		g.drawOval(140,140,120,120);
		g.setColor(new Color(21, 101, 192));
		g.drawOval(160,160,80,80);
		g.setColor(new Color(245, 127, 23));
		g.drawOval(180,180,40,40);
	}
}
