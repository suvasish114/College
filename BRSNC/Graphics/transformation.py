from cmath import cos, sin
import numpy as np
from graphics import *

class Transformation:
    def __init__(self, name, size, color):                  # constractor
        self.window = GraphWin(name, size[0], size[1])      # creating window object
        self.window.setBackground(color)                    # set background color to the canvas
    
    @property
    def close(self):                # close the window 
        self.window.getKey()        # wait for a key to press
        self.window.close()         # destroy the window
    
    def drawTriangle(self, points):
        for i in range(3):
            line = Line(Point(points[i][0], points[i][1]), 
            Point(points[(i+1)%3][0], points[(i+1)%3][1]))
            line.setWidth(3)
            line.draw(self.window)

    def transformationMatrix(self, pivot, angle, translation, scaling):
        ''' Composite transformation matrix of 
            Tranlation (tx, ty) + Rotation (px, py, angle) + Scalling (px, py, sx, xy) + Reflection (wrt x axis)
            Prameters:  pivot (list of int): pivot point of the transformation
                        angle (int): rotation angle in degree
                        translation (2D list of int): translation parameters
                        scaling (2D list of int): scaling parametes '''
        mat = np.array([
            [(scaling[0]*cos(angle)),   (scaling[1]*sin(angle)),    pivot[0]*(1-(scaling[0]*cos(angle)) + (pivot[1]*scaling[1]*sin(angle)) + translation[0])],
            [(scaling[0]*sin(angle)),   -(scaling[1]*cos(angle)),   pivot[1]*(1-(scaling[1]*cos(angle)) + (pivot[0]*scaling[0]*sin(angle)) + translation[1])],
            [0,0,1]])
        return mat
    
    def transformation(self, object, transformationmatrix):
        return np.dot(transformationmatrix, object)

if __name__ == "__main__":
    trans = Transformation("Composit Transformation on Homogenious co-ordinate", [600, 600], "white")
    # trans.drawTriangle([[100,100], [250,150], [300,300]])
    mat = trans.transformationMatrix([1,1], 90, [200,-40], [1.3,1.3])
    triangle = np.array([
        [100,250,300],
        [100, 150, 300],
        [1,1,1]
    ])
    transformed_triangle = trans.transformation(triangle, mat)
    trans.drawTriangle([
        [transformed_triangle[0][0], transformed_triangle[1][0]],
        [transformed_triangle[0][1], transformed_triangle[1][1]],
        [transformed_triangle[0][2], transformed_triangle[1][2]]
    ])
    trans.close
