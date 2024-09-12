"""Paint, for drawing shapes.

Ejericicios

1. Un color nuevo
2. Dibujar un círculo
3. Completar el rectángulo
4. Completar el triángulo
5. Agregar una función para dibujar un pentágono
"""

from turtle import *
from freegames import vector


def line(start, end):
    up()
    goto(start.x, start.y)
    down()
    goto(end.x, end.y)


def square(start, end):
    up()
    goto(start.x, start.y)
    down()
    begin_fill()

    for count in range(4):
        forward(end.x - start.x)
        left(90)

    end_fill()


def circle(start, end):
    """2. Funcion para dibujar un circulo . Autor: Bruno Zamora"""
    up()
    goto(start.x, start.y)
    down()
    begin_fill()
    
    for count in range(360):
        forward(end.x/15 - start.x/15)
        left(1)
    end_fill()


def rectangle(start, end):
    """3. Funcion para dibujar un rectangulo. Autor: Javier Cuatepotzo"""
    up()
    goto(start.x, start.y)
    down()
    begin_fill()

    width = end.x - start.x
    height = end.y - start.y


    for count in range(2):
        forward(width) 
        left(90)
        forward(height)  
        left(90)

    end_fill()


def pentagon(start, end):
    """4. Funcion para dibujar un pentagono. Autor: Anhuar Maldonado"""
    up()
    goto(start.x, start.y)
    down()
    begin_fill()

    for count in range(5):
        forward(end.x - start.x)
        left(72)

    end_fill()

def triangle(start, end):
    """5. Funcion para dibujar un triangulo. Autor: Javier Cuatepotzo"""
    up()
    goto(start.x, start.y)
    down()
    begin_fill()

    for count in range(3):
        forward(end.x - start.x)
        left(120)

    end_fill()

def tap(x, y):
    start = state['start']

    if start is None:
        state['start'] = vector(x, y)
    else:
        shape = state['shape']
        end = vector(x, y)
        shape(start, end)
        state['start'] = None


def store(key, value):
    """Store value in state at key."""
    state[key] = value


state = {'start': None, 'shape': line}
setup(420, 420, 370, 0)
onscreenclick(tap)
listen()
onkey(undo, 'u')
onkey(lambda: color('black'), 'K')
onkey(lambda: color('white'), 'W')
onkey(lambda: color('green'), 'G')
onkey(lambda: color('blue'), 'B')
onkey(lambda: color('red'), 'R')
"""1. Color Magenta agregado. Autor: Bruno Zamora"""
onkey(lambda: color('magenta'), 'M')
onkey(lambda: store('shape', line), 'l')
onkey(lambda: store('shape', square), 's')
onkey(lambda: store('shape', circle), 'c')
onkey(lambda: store('shape', rectangle), 'r')
onkey(lambda: store('shape', triangle), 't')
onkey(lambda: store('shape', pentagon), 'p')
done()