import turtle
import random

turtle.width(3)
turtle.speed(1)

colorlist = ["red", "green", "blue", "red", "yellow"]

def square(size):
    for i in range(4):
        turtle.fd(size)
        turtle.lt(90)

for i in range(100):
    x = random.randrange(-200, 200)
    y = random.randrange(-200, 200)

    turtle.up()
    turtle.goto(x, y)
    turtle.down()

    col = random.choice(colorlist)
    turtle.color(col)

    square(random.randrange(10, 20))

turtle.done()