// compile source: /usr/lib/jvm/java-8-openjdk-amd64/bin/javac <filename>

import java.awt.*;
import java.applet.*;

public class Ball extends Applet{
	private int x = 150;
	private int y = 100;
	private boolean FLAG = false;
	public void paint(Graphics g){
		g.drawRect(100,100,100,100);
		g.setColor(new Color(0, 0, 128));
		g.fillOval(x, y, 10, 10);
		if(this.y == 100) this.FLAG = true;
		else if(this.y == 200-3) this.FLAG = false;
		if(this.FLAG == true){ this.y += 1;}
		else{this.y -= 1;}
		try{Thread.sleep(10);}
		catch(InterruptedException e){}
		repaint();
	}
}
