import java.awt.*;
import java.applet.*;

public class Glass extends Applet{
	public void paint(Graphics g){
		int x1[] = {100,200,150,100};
		int y1[] = {100,100,200,100};
		int x2[] = {100,200,150,100};
		int y2[] = {100,100,200,100};
		g.drawPolyline(x1,y1,4);
		// g.drawLine();
	}
}
