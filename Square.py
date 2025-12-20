import turtle

turtle.bgcolor("red")

t = turtle.Turtle()
t.speed(5)  # not painfully slow, not lightning fast

for _ in range(4):
    t.forward(100)   # length of each side
    t.right(90)      # turn 90 degrees

turtle.done()