import java.applet.*;
import java.awt.*;
import java.awt.event.*;

public class Keyboard extends Applet implements KeyListener{
    String msg = "";
    String whichKey = "";
    public void init(){ addKeyListener(this);}
    public void keyPressed(KeyEvent ke){
        this.whichKey = String.valueOf(ke.getKeyChar());
        if (ke.getKeyCode() == 8) this.msg = this.msg.substring(0,this.msg.length()-1);
        repaint();
    }
    public void keyReleased(KeyEvent ke){
        this.whichKey = "";
    }
    public void keyTyped(KeyEvent ke){
        this.msg += String.valueOf(ke.getKeyChar());
    }
    public void paint(Graphics g){
        g.drawString(this.whichKey,10,10);
        g.drawString(this.msg,10,50);
    }
}
