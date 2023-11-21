from graphics import *

class Bresenham:    # class represents brecenham's line drawing algorithm
    def __init__(self, name = "canvas", size = [500,500], color = "white"):     # constractor
        ''' Initialized class object with window name, window size and color
            Parameters: name (str) : window name (default = 'canvas')
                        size (list of int) : window size (default 500 X 500)
                        color (str) : window background color (default = 'white')
        '''
        self.window = GraphWin(name, size[0], size[1])  # creating canvas with defined size
        self.window.setBackground(color)    # set background color
    
    def drawPixel(self, corx, cory):    # function to draw a single pixel
        '''	A function to draw a single pixel in 2d co-ordinate canvus
		    Parameters:	corx (int) = x co-ordinate point
			    	    cory (int) = y co-ordinate point
		    Return:	None
	    '''
        point = Point(corx, cory)
        point.draw(self.window)

    def draw(self, start, end):
        ''' Draw the line using bresenham's algorithm
            Parameters :    start (1D list) : start index
                            end (1D list) : end index
            Return : None        
        '''
        dx = abs(start[0] - end[0])
        dy = abs(start[1] - end[1])
        x = start[0]    # start coordinate x axis
        y = start[1]    # start co-ordinate y axis
        p = 0   # decission parameter
        if dx >= dy:
            p = (2*dy) - dx
            for i in range(dx):
                x += 1
                if p >= 0:
                    y += 1
                    p += (2*dy) - (2*dx)
                else:
                    p += (2*dy)
                self.drawPixel(x,y)
                
        else:
            p = (2*dx) - dy
            for i in range(dy):
                y += 1
                if p >= 0:
                    x += 1
                    p += (2*dx) - (2*dy)
                else:
                    p += 2*dx
                self.drawPixel(x,y)
    
    @property
    def close(self):     # function to close the window
        self.window.getKey()    # wait for a key to press
        self.window.close()     # close the window
    
    def __repr__(self) -> str:
        pass

if __name__ == "__main__":  # driving code
    line = Bresenham("Bresenham's Line Drawing Algorithm", [400,400], "white")      # bresenham classs object creation
    line.draw([100,50],[200,300])       # draw line using draw function
    line.close      # close the window until key pressed or using close button