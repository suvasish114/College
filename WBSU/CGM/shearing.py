import turtle
import numpy as np

# translate matrix
def shearing(coor, shearing_pixel):
    ipcoor = np.vstack((np.array(coor).transpose(), np.array([1,1,1,1])))
    shearing_matrix = np.array([
        [1,shearing_pixel,-(shearing_pixel*(-1))],
        [0,1,0],
        [0,0,1]
    ])
    return np.dot(shearing_matrix, ipcoor)

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
    ipcoor = list(list(map(int, input(f"Coordinate {i+1}: ").strip().split(" "))) for i in range(4))
    shearing_pixel = int(input("Shearing pixel: "))
    opcoor = shearing(ipcoor, shearing_pixel)

    tr = turtle.Turtle()
    tr.hideturtle()
    tr.speed(0)

    # draw X Y coordinates
    drawxycoor(tr)

    # # draw initial object before transformation
    turtle.title("before")
    tr.color("gray")
    tr.penup()
    tr.goto(ipcoor[0][0],ipcoor[0][1])
    tr.pendown()
    tr.begin_fill()
    tr.goto(ipcoor[1][0],ipcoor[1][1])
    tr.goto(ipcoor[2][0],ipcoor[2][1])
    tr.goto(ipcoor[3][0],ipcoor[3][1])
    tr.goto(ipcoor[0][0],ipcoor[0][1])
    tr.end_fill()

    # draw final object after transformation
    # turtle.title("after")
    # tr.color("gray")
    # tr.penup()
    # tr.goto(opcoor[0][0],opcoor[1][0])
    # tr.pendown()
    # tr.begin_fill()
    # tr.goto(opcoor[0][1],opcoor[1][1])
    # tr.goto(opcoor[0][2],opcoor[1][2])
    # tr.goto(opcoor[0][3],opcoor[1][3])
    # tr.goto(opcoor[0][0],opcoor[1][0])
    # tr.end_fill()

    turtle.done()
