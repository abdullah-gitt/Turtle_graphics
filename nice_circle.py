from Doreamon import my_goto
import turtle 
turtle.pen()
for i in range(1):
    turtle.speed(3)
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
    
if __name__ == '__main__':
    turtle.screensize(1000, 1000, "#f0f0f0")
    turtle.pensize(3)
    turtle.speed(9)

    ()

    my_goto(-400, -400)
    turtle.write(' Created by>Abdullah Al Mahmud by coding in Python', font=("Bradley Hand ITC", 32, "bold"))

turtle.done()
