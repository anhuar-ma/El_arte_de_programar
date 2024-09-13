from random import randrange
from turtle import *

from freegames import vector

ball = vector(-200, -200)
speed = vector(0, 0)
targets = []

def tap(x, y):
    """Respond to screen tap."""
    if not inside(ball):
        ball.x = -199
        ball.y = -199
        speed.x = (x + 200) / 25
        speed.y = (y + 200) / 25

def inside(xy):
    """Return True if xy within screen."""
    return -200 < xy.x < 200 and -200 < xy.y < 200

def draw_square(size, color):
    """Draw a square of a given size and color."""
    begin_fill()
    fillcolor(color)
    for _ in range(4):
        forward(size)
        left(90)
    end_fill()

def draw_hexagon(size, color):
    """Draw a hexagon of a given size and color."""
    begin_fill()
    fillcolor(color)
    for _ in range(6):
        forward(size)
        left(60)  # Ángulo interno de un hexágono
    end_fill()

def draw():
    """Draw ball and targets."""
    clear()

    for target in targets:
        goto(target.x, target.y)
        draw_square(20, 'black')  # Los balones son cuadrados amarillos

    if inside(ball):
        goto(ball.x, ball.y)
        draw_hexagon(10, 'green')  # Los proyectiles son hexágonos verdes

    update()

def move():
    """Move ball and targets."""
    if randrange(40) == 0:
        y = randrange(-150, 150)
        target = vector(200, y)
        targets.append(target)

    for target in targets:
        target.x -= 0.5

    if inside(ball):
        speed.y -= 0.35
        ball.move(speed)

    dupe = targets.copy()
    targets.clear()

    for target in dupe:
        if abs(target - ball) > 13:
            targets.append(target)

    draw()

    for target in targets:
        if not inside(target):
            #se elimina el target y se agrega uno nuevo
            targets.remove(target)
            targets.append(vector(200, randrange(-150, 150)))

    ontimer(move, 10)

setup(420, 420, 370, 0)
hideturtle()
up()
tracer(False)
onscreenclick(tap)
move()
done()
