import turtle
import numpy as np
import math

# translate matrix
def scalling(coor, scalling_vector):
    ipcoor = np.vstack((np.array(coor).transpose(), np.array([1,1,1])))
    scalling_matrix = np.array([
        [scalling_vector[0], 0, 0],
        [0, scalling_vector[1], 0],
        [0,0,1]
    ])
    return np.dot(scalling_matrix, ipcoor)

# draw XY coordinates
def drawxycoor(tr):
    tr.forward(1000)
    tr.backward(2000)
    tr.forward(1000)
    tr.left(90)
    tr.forward(1000)
    tr.backward(2000)
    tr.forward(1000)
    tr.right(90)

# driving code
if __name__ == "__main__":
    ipcoor = list(list(map(int, input(f"Coordinate {i+1}: ").strip().split(" "))) for i in range(3))
    scalling_vector = list(map(int, input("(Sx, Sy): ").strip().split(" ")))
    opcoor = scalling(ipcoor, scalling_vector)

    tr = turtle.Turtle()
    tr.hideturtle()
    tr.speed(0)

    # draw X Y coordinates
    drawxycoor(tr)

    # draw final object after transformation
    '''
    turtle.title("after")
    tr.color("gray")
    tr.penup()
    tr.goto(opcoor[0][0],opcoor[1][0])
    tr.pendown()
    tr.begin_fill()
    tr.goto(opcoor[0][1],opcoor[1][1])
    tr.goto(opcoor[0][2],opcoor[1][2])
    tr.goto(opcoor[0][0],opcoor[1][0])
    tr.end_fill()
    '''

    # draw initial object before transformation
    turtle.title("before")
    tr.color("gray")
    tr.penup()
    tr.goto(ipcoor[0][0],ipcoor[0][1])
    tr.pendown()
    tr.begin_fill()
    tr.goto(ipcoor[1][0],ipcoor[1][1])
    tr.goto(ipcoor[2][0],ipcoor[2][1])
    tr.goto(ipcoor[0][0],ipcoor[0][1])
    tr.end_fill()

    turtle.done()
