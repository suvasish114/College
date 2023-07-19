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

def drawWindow(tr, _from, _to):
	tr.penup()
	tr.goto(_from[0],_from[1])
	tr.pendown()
	tr.goto(_to[0],_from[1])
	tr.goto(_to[0],_to[1])
	tr.goto(_from[0],_to[1])
	tr.goto(_from[0],_from[1])

def drawObject(tr,coor):
	tr.penup()
	tr.goto(coor[0],coor[1])
	tr.pendown()
	tr.color("BLACK")
	tr.begin_fill()
	tr.circle(5)
	tr.end_fill()

def algorithm(window_from, window_to, coor):
	xw_min = window_from[0][0]
	xw_max = window_from[1][0]
	yw_min = window_from[0][1]
	yw_max = window_from[1][1]
	xv_min = window_to[0][0]
	xv_max = window_to[1][0]
	yv_min = window_to[0][1]
	yv_max = window_to[1][1]
	xw = coor[0]
	yw = coor[1]
	xv = 0
	yv = 0
	xv = xv_min+((xw - xw_min)*((xv_max - xv_min)/(xw_max - xw_min)))
	yv = yv_min+((yw - yw_min)*((yv_max - yv_min)/(yw_max - yw_min)))
	return abs(xv),abs(yv)

if __name__ == "__main__":
	window1 = [list(map(int, input("From: ").strip().split(" "))) for _ in range(2)]
	window2 = [list(map(int, input("To: ").strip().split(" "))) for _ in range(2)]
	[x,y] = list(map(int,input("Object: ").strip().split(" ")))
	tr = turtle.Turtle()
	turtle.title("After")
	tr.ht()
	tr.speed(0)
	draw_axis(tr)
	tr.color("RED")
	# drawWindow(tr, window1[0],window1[1])
	tr.color("BLUE")
	drawWindow(tr, window2[0],window2[1])
	# drawObject(tr, [x,y])
	_x,_y = algorithm(window1, window2, [x,y])
	drawObject(tr, [_x,_y])
	turtle.done()
