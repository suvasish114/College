# file: ddl.py
from graphics import *

class DDL:              # class represent DDL line drawing algorithm
    def __init__(self, name, canvas_size, canvas_color):
        ''' Parameter:  name (str) = name of the canvas
                        canvas_size (1d list) = size of the canvas
                        canvas_color (str) = color of the canvas
            Return: None
        '''
        self.window = GraphWin(name, canvas_size[0], canvas_size[1])    # drawing a 400 X 400 canvus
        self.window.setBackground(canvas_color)                         # set canvas background color white

    def drawPixel(self, corx, cory):            # function to draw a single pixel
        '''	A function to draw a single pixel in 2d co-ordinate canvus
		    Parameters:	corx (int) = x co-ordinate point
			    	    cory (int) = y co-ordinate point
		    Return:	None
	    '''
        point = Point(corx, cory)
        point.draw(self.window)

    def draw(self, x1, y1, x2, y2):             # function to draw line
        ''' This function draw a straight line from co-ordinate (x1,y1) to (x2,y2)
            Parameters: x1, y1 (int, int) = 1st co-ordinate
                        x2, y2 (int, int) = 2nd co-ordinate
            Return: None
        ''' 
        dx = x2 - x1
        dy = y2 - y1
        x = x1
        y = y1
        steps = abs(dy)         # calculating steps to loop the code
        xinc = abs(dx / steps)  # how many pixels to skip for x
        yinc = abs(dy / steps)  # how many pixels to skip for y
        for i in range(steps):  # loop from 0 to steps
            self.drawPixel(x, y)    # draw a single pixel
            x += xinc
            y += yinc

    @property           # to call as a proprty
    def closeWindow(self):      # function to close the canvas
        self.window.getKey()    # wait for a key to press
        self.window.close()     # close the window


# driving code
if __name__ == "__main__":  # driving code
    obj = DDL("DDL line drawing algorithm", [400,400], "white") # creating DDL class object
    obj.draw(100, 100, 300, 300)    # draw a stright line from (100,100) to (300,300)
    obj.closeWindow             # close the window