#Exercise 4-19 Stop Sign
#Varun sri ram muniganti
#CS175L



import turtle
s=8
l=90
a= 360/s
x=0
diameter= s+2*x
turtle.setup(400,400)
turtle.penup()
turtle.goto(-50,-60)
turtle.pendown()
turtle.pensize(10)
turtle.color('black','red')
turtle.begin_fill()
for x in range(s):
    turtle.pendown()
    turtle.forward(l)
    turtle.left(a)
turtle.end_fill()
turtle.penup()
turtle.goto(-72,20)
turtle.color('white')
turtle.write('STOP',font=('Times New Roman', 45))



