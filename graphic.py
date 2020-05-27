import turtle
do=turtle.Turtle()
do.speed(78)
do.goto(-180,0)
do.color("black","light blue")
do.begin_fill()
for i in range(50):
	do.forward(90*4)
	do.left(168)
	do.forward(100*4)
	do.right(189)
	if i==33:
		do.end_fill()
turtle.done()