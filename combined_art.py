import turtle
turtle.pen()
for i in range(8):
    turtle.speed(0)
    turtle.fd(100)
    turtle.lt(225)
    turtle.color('red')
turtle.reset()
for i in range(20):
    turtle.color('blue', 'green')
    turtle.width(3)
    turtle.speed(0)
    turtle.circle(5 * i) 
    turtle.lt(180)   
turtle.reset()
for i in range(1):

    turtle.speed(2)
    turtle.width(30)
    turtle.color('blue')
    turtle.circle(150)
    turtle.lt(180)
    turtle.color('red')
    turtle.circle(150) 
    turtle.lt(270)
    turtle.color('yellow')
    turtle.circle(150)
    turtle.lt(180)
    turtle.color('black')
    turtle.circle(150)
    
    
    turtle.done()