import turtle

screen = turtle.Screen()
screen.bgcolor("white")
screen.title("Colorful Audi Logo")

t = turtle.Turtle()
t.speed(5)
t.pensize(8)
t.hideturtle()


def draw_ring(x, y, radius, color):
    t.penup()
    t.goto(x, y - radius)
    t.setheading(0)
    t.pendown()
    t.color(color)
    t.circle(radius)


radius = 80
spacing = 65

draw_ring(-spacing * 1.5, 0, radius, "red")
draw_ring(-spacing * 0.5, 0, radius, "blue")
draw_ring(spacing * 0.5, 0, radius, "green")
draw_ring(spacing * 1.5, 0, radius, "orange")

turtle.done()