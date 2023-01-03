import turtle

t = turtle.Turtle()

def stairs(size, nb):
    global t
    steps = 0
    while steps < nb:
        steps += 1
        t.forward(size)
        t.left(90)
        t.forward(size)
        t.right(90)

    t.forward(size)


def sqaure(size):
    global t
    for i in range(0,4):
        t.forward(size)
        t.left(90)

def sqaures(beginning_size, nb):
    for i in  range(0,nb):
        sqaure((i+1)*beginning_size)

# stairs(60, 4)
# sqaure(50)
sqaures(50, 5)
turtle.done()