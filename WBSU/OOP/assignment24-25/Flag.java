// compile source: /usr/lib/jvm/java-8-openjdk-amd64/bin/javac <filename>
import java.applet.*;
import java.awt.*;

public class Flag extends Applet{
	public void paint(Graphics g){
		g.setColor(new Color(255, 153, 51));
		g.fillRect(100, 100, 400, 100);

		g.setColor(new Color(255, 255, 255));
		g.fillRect(100, 200, 400, 100);

		g.setColor(new Color(19, 136, 8));
		g.fillRect(100, 300, 400, 100);

		g.setColor(new Color(0, 0, 128));
		g.drawOval(250, 200, 100, 100);

		int d = 15, x = 300, y = 250;
		double r = 50, a, b;

		for(int i=0; i<=6; i++){
			a = r*Math.cos(Math.toRadians(15)*i);
			b = r*Math.sin(Math.toRadians(15)*i);
			g.drawLine(x, y, x+(int)a, y+(int)b);
			g.drawLine(x, y, x+(int)a, y-(int)b);
			g.drawLine(x, y, x-(int)a, y+(int)b);
			g.drawLine(x, y, x-(int)a, y-(int)b);
		}
    }
}
