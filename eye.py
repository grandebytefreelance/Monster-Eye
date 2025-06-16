import turtle 
turtle.bgcolor("green")

p = turtle.Turtle()
pb = turtle

p.up()
p.goto(0,-150)               
p.color('white')               
p.begin_fill()                 
p.circle(360)                   
p.end_fill()


p.up()
p.goto(0,-100)               
p.color('red')               
p.begin_fill()                 
p.circle(300)                   
p.end_fill()

p.up()
p.goto(-1,60)
p.color('black')
p.begin_fill ()
p.circle(150)
p.end_fill()

p.up()
p.goto(1,70)
p.color('white')
p.begin_fill ()
p.circle(100)
p.end_fill()

pb.done()