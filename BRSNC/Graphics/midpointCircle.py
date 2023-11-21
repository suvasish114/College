# demonstration of midpoint circle drawing algorithm
from graphics import *

class MidpointCircle:
    def __init__(self, name, size, color):      # constractor
        self.window = GraphWin(name, size[0], size[1])
        self.window.setBackground(color)

    def drawPixel(self, corx, cory):    # function to draw a single pixel
        '''	A function to draw a single pixel in 2d co-ordinate canvus
		    Parameters:	corx (int) = x co-ordinate point
			    	    cory (int) = y co-ordinate point
		    Return:	None
	    '''
        point = Point(corx, cory)   # get a point on the 2D co-ordinate
        point.draw(self.window)     # draw the point

    def circlePoint(self, x, y, center):    # draw 8 pixel respect to the 1st co-ordinate point
        ''' A function to draw 8 point on 4 co-ordinate on a 2D plane with respect to the 1st co-ordinate point
            Parameters: x (int) : x axis
                        y (int) : y axis
                        center (list of int) : center point of the circle
            Returns :   None
        '''
        self.drawPixel(center[0] + x, center[1] + y)
        self.drawPixel(center[0] + y, center[1] + x)
        self.drawPixel(center[0] - y, center[1] + x)
        self.drawPixel(center[0] + x, center[1] - y)
        self.drawPixel(center[0] - x, center[1] + y)
        self.drawPixel(center[0] + y, center[1] - x)
        self.drawPixel(center[0] - x, center[1] - y)
        self.drawPixel(center[0] - y, center[1] - x)

    def draw(self, radius, center):     # algorithm
        ''' A function to draw circle using midpoint circle drawing algorithm
            Parametes : radius (int) : radius of the circle
                        center (list of int) : center of the circle
            Returns :   None
        '''
        y = radius
        x = 0 
        d = 1 - radius  # decission parameter
        self.circlePoint(x,y, center)
        while y > x:
            x += 1
            if d >= 0:
                y -= 1
                d += 2*x - 2*y + 5
            else:
                d += 2*x + 3
            self.circlePoint(x,y, center)
    
    @property
    def close(self):            # close the window
        self.window.getKey()    # wait until a key pressed
        self.window.close()     # close the window
    
if __name__ == "__main__":  # driving code
    circle = MidpointCircle("Midpoint Circle Drawing Algorithm", [500,500], "white")    # creating object of MidpointCircle class
    circle.draw(100, [250, 250])    # draw the circle 
    circle.close        # close the window