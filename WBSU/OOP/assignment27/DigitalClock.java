// compile source: /usr/lib/jvm/java-8-openjdk-amd64/bin/javac <filename>
import java.applet.*;
import java.awt.*;
import java.time.LocalTime;

public class DigitalClock extends Applet{
    public void paint(Graphics g){
        g.drawRect(100, 100, 100, 50);
        g.drawString(String.valueOf(LocalTime.now()), 110, 130);
        try{Thread.sleep(1000);}
        catch(InterruptedException e){}
        repaint();
    }
}
