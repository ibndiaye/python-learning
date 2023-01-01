import turtle


def stairs(size, nb):
    for i in range(0, nb):
        t.forward(size)
        t.left(90)
        t.forward(size)
        t.right(90)
    t.forward(size)


def square(size):
    for i in range(0, 4):
        t.forward(size)
        t.left(90)


def squares(beginning_size, nb):
    # 10 / 20 / 30 / 40
    # size = (i+1)*beginning_size
    for i in range(0, nb):
        size = (i + 1) * beginning_size
        square(size)


t = turtle.Turtle()

# stairs(60, 4)
# square(100)
squares(10, 10)

turtle.done()
