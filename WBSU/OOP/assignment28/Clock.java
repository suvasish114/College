import java.awt.*;
import java.applet.*;
import java.time.LocalTime;

public class Clock extends Applet{
	int hour, minute, second, i = 0, j = 0, k = 0;
	double r=100, a, b;
	
	public void paint(Graphics g){
		Graphics2D g2 = (Graphics2D) g;
		g.drawOval(100,100,200,200);
		
		hour = LocalTime.parse(String.valueOf(LocalTime.now())).getHour();
		minute = LocalTime.parse(String.valueOf(LocalTime.now())).getMinute();
		second = LocalTime.parse(String.valueOf(LocalTime.now())).getSecond();
		
		// draw lines
		for(int i=0; i<12; i++){
			a = (r+10) * Math.cos(Math.toRadians(30)*i);
			b = (r+10) * Math.sin(Math.toRadians(30)*i);
			g.drawString(String.valueOf(i+1),195+(int)a,205+(int)b);
		}
		
		// for second
		a = r * Math.cos(Math.toRadians(6)*second);
		b = r * Math.sin(Math.toRadians(6)*second);
		g.drawLine(200,200,200+(int)a,200+(int)b);

		// for minute
		g2.setStroke(new BasicStroke(3));
		a = (r-20) * Math.cos(Math.toRadians(6)*minute);
		b = (r-20) * Math.sin(Math.toRadians(6)*minute);
		g2.drawLine(200,200,200+(int)a,200+(int)b);
		
		// for hour
		g2.setStroke(new BasicStroke(7));
		a = (r-30) * Math.cos(Math.toRadians(6)*hour);
		b = (r-30) * Math.sin(Math.toRadians(6)*hour);
		g2.drawLine(200,200,200+(int)a,200+(int)b);
		
		// reload
		try{Thread.sleep(1000);}
		catch(InterruptedException e){}
		repaint();
	}
}
