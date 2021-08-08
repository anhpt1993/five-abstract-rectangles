import turtle as t

def rectangle(x):
    t.pendown()
    t.forward(x/2)
    t.right(90)
    for i in range(3):
        t.forward(x)
        t.right(90)
    t.forward(x/2)

t.speed(5)
t.pensize(3)
t.dot(10,"black")
t.hideturtle()
t.left(90)

for i in range(5):
    rectangle(100)
    t.right(72)

t.done()