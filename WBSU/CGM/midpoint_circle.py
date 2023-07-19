# MIDPOINT LINE DRAWING ALGORITHM
import turtle

def draw_axis(tr):
	tr.forward(1000)
	tr.backward(2000)
	tr.forward(1000)
	tr.left(90)
	tr.forward(1000)
	tr.backward(2000)
	tr.forward(1000)
	tr.right(90)

def drawpixel(tr,coor):
	tr.penup()
	tr.goto(coor[0], coor[1])
	tr.pendown()
	tr.dot()

def drawsymmetry(tr, coor):
	drawpixel(tr,[coor[0],coor[1]])
	drawpixel(tr,[coor[1],coor[0]])
	drawpixel(tr,[-coor[0],coor[1]])
	drawpixel(tr,[-coor[1],coor[0]])
	drawpixel(tr,[coor[0],-coor[1]])
	drawpixel(tr,[coor[1],-coor[0]])
	drawpixel(tr,[-coor[0],-coor[1]])
	drawpixel(tr,[-coor[1],-coor[0]])

def midpoint_circle(r,tr):
	draw_axis(tr)
	tr.width(3)
	tr.penup()
	tr.goto(0,r)
	tr.pendown()
	tr.speed(0)
	x = 0
	y = r
	d = 1-r
	while y>=x:
		x += 1
		if d >= 0:
			y -= 1
			d += (2*x)-(2*y)+5
		else:
			d += (2*x)+3
		drawsymmetry(tr, [x,y])

# driving code
if __name__ == "__main__":
	radius = int(input("radius: "))
	turtle.title("Midpoing Circle")
	tr = turtle.Turtle()
	tr.hideturtle()
	tr.speed(0)
	midpoint_circle(radius,tr)
	turtle.done()
