import java.applet.*;
import java.awt.event.*;
import java.util.*;
import java.awt.*;

public class Mouse extends Applet implements MouseListener, MouseMotionListener{
    private String msg;
    private String coor;
    private int x;
    private int y;
    public void init(){
        addMouseListener(this);
        addMouseMotionListener(this);
    }
    public void mouseClicked(MouseEvent me){
        msg = "Mouse Clicked";
        coor = "("+String.valueOf(x)+","+String.valueOf(y)+")";
        x = me.getX();
        y = me.getY();
        repaint();
    }
    public void mouseEntered(MouseEvent me){
        msg = "Mouse Entered";
        repaint();
    }
    public void mouseExited(MouseEvent me){
        msg = "Mouse Exited";
        repaint();
    }
    public void mousePressed(MouseEvent me){
        msg = "Mouse Pressed";
        repaint();
    }
    public void mouseReleased(MouseEvent me){
        msg = "Mouse Released";
        repaint();
    }
    public void mouseDragged(MouseEvent me){
        msg = "Mouse Dragged";
        repaint();
    }
    public void mouseMoved(MouseEvent me){
        coor = "("+String.valueOf(x)+","+String.valueOf(y)+")";
        repaint();
    }
    public void paint(Graphics g) {
        g.drawString(this.msg,100,100);
        g.drawString(this.coor,x,y);
    }
}
