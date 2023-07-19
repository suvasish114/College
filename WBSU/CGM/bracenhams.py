import turtle as tr

# configuration
tr.width(1)
tr.hideturtle()
tr.speed(0)

# draw x-y axis
def axis(tr):
    tr.forward(1000)
    tr.backward(2000)
    tr.forward(1000)
    tr.left(90)
    tr.forward(1000)
    tr.backward(2000)
    tr.forward(1000)

# draw a single pixel
def drawPixel(coordinate):
    tr.goto(coordinate[0], coordinate[1])

# bracenhams algorithm
def bracenhams(from_coordinate, to_coordinate):
    tr.penup()
    tr.goto(from_coordinate[0],from_coordinate[1])
    tr.pendown()

    # variables
    x1 = from_coordinate[0]     # initial co-ordinate x
    y1 = from_coordinate[1]     # initial co-ordinate y
    x2 = to_coordinate[0]       # final co-ordinate x
    y2 = to_coordinate[1]       # final co-ordinate y
    dx = x2-x1                  # rate of change in x
    dy = y2-y1                  # rate of change in y
    x = x1                      # instantanious axis x
    y = y1                      # instantanious axis y
    p = (2*dy) - dx             # initial decission parameter
    
    drawPixel([x,y])            # initial pixel

    # loop
    for i in range(dx):
        x += 1
        if p>=0:
            y += 1
            p = (2*dy) - (2*dx)
        else:
            p = (2*dy) - dx
        drawPixel([x,y])

# driving code
if __name__ == "__main__":
    tr.color("red")
    axis(tr)
    tr.color("black")
    tr.width(3)
    bracenhams([10,20],[150,180])
    tr.done()

