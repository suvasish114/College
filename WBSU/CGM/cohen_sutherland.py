import turtle

xmin = 0
ymin = 0
xmax = 50
ymax = 50

def drawLine(tr, _from, _to):
	tr.penup()
	tr.goto(_from[0],_from[1])
	tr.pendown()
	tr.goto(_to[0],_to[1])
	
def compute_region(x, y):
	CENTER = 0
	LEFT = 1
	RIGHT = 2
	BOTTOM = 4
	TOP = 8
	
	code = 0
	
	if x < xmin:
		code = code | LEFT
	elif x > xmax:
		code = code | RIGHT
	if y < ymin:
		code = code | BOTTOM
	elif y > ymax:
		code = code | TOP
		
	return code

def clip(_from, _to):
	code1 = compute_region(_from[0], _from[1])
	code2 = compute_region(_to[0], _to[1])
	is_accepted = False
	x = 0
	y = 0
	while True:
		if code1 == 0 and code2 == 0:
			is_accepted = True
			return _from, _to
		elif (code1 and code2) != 0:
			return None
		else:
			code = None
			if code1 != 0:
				code = code1
			else:
				code = code2
			
			# find region
			if code & 1:	# LEFT
				x = xmin
				y = (_from[1])+((xmin-_from[0])*((_to[0]-_from[0])/(_to[1]-_from[1])))
			elif code & 2:	# RIGHT
				x = xmax
				y = ((_to[0]-_from[0])/(_to[1]-_from[1]))
			elif code & 4:	# BOTTOM
				y = ymin
				x = ((_to[0]-_from[0])/(_to[1]-_from[1]))
			elif code & 8:	# TOP
				y = ymax
				x = ((_to[0]-_from[0])/(_to[1]-_from[1]))



if __name__ == "__main__":
	_from = list(map(int, input("From: ").strip().split()))
	_to = list(map(int, input("To: ").strip().split()))
	# take window as 50x50
	turtle.speed(0)
	tr = turtle.Turtle()
	tr.ht()
	drawLine(tr, _from, _to)
	__from, __to = clip(_from, _to)
	tr.color("RED")
	drawLine(tr, __from, __to)
	turtle.done()
