// compile source: /usr/lib/jvm/java-8-openjdk-amd64/bin/javac <filename>
// /usr/lib/jvm/java-8-openjdk-amd64/bin/javac
import java.applet.*;
import java.awt.*;

public class Banner extends Applet{
    public void paint(Graphics g){
        g.drawString("Hello Applet", 20, 20);
    }
}
