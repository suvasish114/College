# Line clipping using Cohen–Sutherland line clipping algorithm
from graphics import *

class CohenSutherland: 
    # Defining region codes 
    INSIDE = 0  # 0000 
    LEFT = 1    # 0001 
    RIGHT = 2   # 0010 
    BOTTOM = 4  # 0100 
    TOP = 8     # 1000 

    def __init__(self, name, size, color):  # constructor
        ''' Represents Cohen Sitherland line clipping algorithm class.
            Parameters : name (str) : name of the window
                         size (2D list of int) : size of the window
                         color (str) : window background color '''

        self.window = GraphWin(name, size[0], size[1])
        self.window.setBackground(color)

    def computeRegion(self, x, y):
        ''' Compute the region code using biteise OR operation
            Parameters: x (int): x axis
                        y (int): y axis
            Return: region code of the point '''

        code = self.INSIDE
        if x < self.x_min:      # to the left of rectangle 
            code |= self.LEFT 
        elif x > self.x_max:    # to the right of rectangle 
            code |= self.RIGHT 
        if y < self.y_min:      # below the rectangle 
            code |= self.BOTTOM 
        elif y > self.y_max:    # above the rectangle 
            code |= self.TOP 
    
        return code
    
    def clip(self):
        ''' clip the calling objects straight line with respect to the calling objects window. Find intersection point using formulas
                y = y1 + slope * (x - x1),  
                x = x1 + (1 / slope) * (y - y1)
                where slope is (y2-y1)/(x2-x1) '''

        code1 = self.computeRegion(self.x1, self.y1)
        code2 = self.computeRegion(self.x2, self.y2)

        accept = False

        while True:
            if code1 == 0 and code2 == 0:       # if line is inside the window
                accept = True
                break
            elif (code1 & code2) != 0:          # if line is not inside the window
                break 
            
            else:       # line is partially inside the window
                x = 0
                y = 0

                if code1 != 0:
                    code_out = code1
                else:
                    code_out = code2 
                
                if code_out & self.TOP:     # point is the top of the window
                    x = self.x1 + ((self.x2 - self.x1)/(self.y2 - self.y1)) * (self.y_max - self.y1)
                    y = self.y_max

                elif code_out & self.BOTTOM:    # point is the bottom of the window
                    x = self.x1 + ((self.x2 - self.x1)/(self.y2 - self.y1)) * (self.y_min - self.y1)
                    y = self.y_min

                elif code_out & self.RIGHT:     # point is the right of the window
                    x = self.x_max
                    y = self.y1 + ((self.y2 - self.y1)/(self.x2 - self.x1)) * (self.x_max - self.x1)

                elif code_out & self.LEFT:      # point is the left of tht window
                    x = self.x_min
                    y = self.y1 + ((self.y2 - self.y1)/(self.x2 - self.x1)) * (self.x_min - self.x1)

                if code_out == code1:
                    self.x1 = x
                    self.y1 = y
                    code1 = self.computeRegion(self.x1, self.y1)

                else:
                    self.x2 = x
                    self.y2 = y 
                    code2 = self.computeRegion(self.x2, self.y2)
    
    def drawLine(self, start, end):
        ''' Initialize and draw a straight line on the canvas 
            Parameters: start (list of int): strting co-ordinate of the line 
                        end (list of int): ending co-ordinate of the line
            Returns: None '''

        self.x1 = start[0]
        self.y1 = start[1]
        self.x2 = end[0]
        self.y2 = end[1]

        self.clip()     # clip the line

        line = Line(Point(self.x1,self.y1), Point(self.x2, self.y2))
        line.setWidth(3)
        line .draw(self.window)

    
    def drawRectangle(self, start, end):
        ''' Draw a red rectangular window frame
            Parameters: start (list of int): strting co-ordinate of the line 
                        end (list of int): ending co-ordinate of the line
            Returns: None '''

        self.x_min = start[0]
        self.y_min = start[1]
        self.x_max = end[0]
        self.y_max = end[1]

        rect = Rectangle(Point(self.x_min,self.y_min), Point(self.x_max, self.y_max))
        rect.setOutline("red")
        rect.draw(self.window) 

    @property
    def close(self):            # close the window
        self.window.getKey()    # wait for a key to pressed 
        self.window.close()     # destroy the window
    
if __name__ == "__main__":      # driving code
    clipping  = CohenSutherland("Cohen–Sutherland line clipping algorithm", [400,400], "white") # cohensutherland object creation
    clipping.drawRectangle([100,100], [300,300])        # draw clipping window
    clipping.drawLine([50,100], [350,290])              # draw clipped line with respect to the window
    clipping.close                                      # close the window

