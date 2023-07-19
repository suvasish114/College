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

def drawpixel(tr, coor):
	tr.goto(coor[0], coor[1])

def midpoint_line(tr, _from, _to):
	dx = abs(_from[0]-_to[0])
	dy = abs(_from[1]-_to[1])
	a = dy
	b = -dx
	x = _from[0]
	y = _from[1]
	d = a + (b/2)
	tr.penup()
	tr.goto(x,y)
	tr.pendown()
	for k in range(dx):
		x += 1
		if d>=0:
			y += 1
			d += a+b
		else:
			d += a
		drawpixel(tr, [x,y])

if __name__ == "__main__":
	fromcoor = list(map(int, input("From: ").strip().split(" ")))
	tocoor = list(map(int, input("From: ").strip().split(" ")))
	tr = turtle.Turtle()
	tr.ht()
	tr.speed(0)
	draw_axis(tr)
	tr.width(3)
	turtle.title("Midpoing Line")
	midpoint_line(tr, fromcoor, tocoor)
	turtle.done()