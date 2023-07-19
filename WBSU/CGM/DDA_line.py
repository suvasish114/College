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
	tr.goto(abs(coor[0]), abs(coor[1]))

def algorithm(tr, _from, _to):
	dx = abs(_from[0]-_to[0])
	dy = abs(_from[1]-_to[1])
	steps = 0
	if dx > dy:
		steps = dx
	else:
		steps = dy
	xinc = dx/steps
	yinc = dy/steps
	x = _from[0]
	y = _from[1]
	tr.penup()
	tr.goto(x,y)
	tr.pendown()
	for i in range(steps):
		drawpixel(tr,[x,y])
		x += xinc
		y += yinc

if __name__ == "__main__":
	_from = list(map(int, input("From: ").strip().split(" ")))
	_to = list(map(int, input("To: ").strip().split(" ")))
	tr = turtle.Turtle()
	tr.ht()
	tr.speed(0)
	draw_axis(tr)
	tr.width(3)
	algorithm(tr, _from, _to)
	turtle.done()
