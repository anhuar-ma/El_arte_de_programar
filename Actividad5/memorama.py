from random import *
from turtle import *

from freegames import path

car = path('car.gif')
tiles = list(range(32)) * 2
state = {'mark': None}
hide = [True] * 64
tap_count = 0  # Variable para contar los taps

def square(x, y):
    """Draw white square with black outline at (x, y)."""
    up()
    goto(x, y)
    down()
    color('black', 'white')
    begin_fill()
    for count in range(4):
        forward(50)
        left(90)
    end_fill()

def index(x, y):
    """Convert (x, y) coordinates to tiles index."""
    return int((x + 200) // 50 + ((y + 200) // 50) * 8)

def xy(count):
    """Convert tiles count to (x, y) coordinates."""
    return (count % 8) * 50 - 200, (count // 8) * 50 - 200

def tap(x, y):
    """Update mark and hidden tiles based on tap."""
    global tap_count  # Declarar la variable global
    spot = index(x, y)
    mark = state['mark']
    tap_count += 1  # Incrementar el conteo de taps
    print(f'Taps: {tap_count}')  # Imprimir el conteo de taps en la consola

    if mark is None or mark == spot or tiles[mark] != tiles[spot]:
        state['mark'] = spot
    else:
        hide[spot] = False
        hide[mark] = False
        state['mark'] = None

def draw():
    """Draw image and tiles."""
    clear()
    goto(0, 0)
    shape(car)
    stamp()

    for count in range(64):
        if hide[count]:
            x, y = xy(count)
            square(x, y)

    mark = state['mark']

    if mark is not None and hide[mark]:
        x, y = xy(mark)
        up()
        goto(x + 25, y + 13)  # Ajuste para centrar el número en el cuadrado
        color('black')
        write(tiles[mark], align="center", font=('Arial', 20, 'normal'))  # Centrar el número

    # Detectar si todos los cuadros han sido revelados
    if all(not hidden for hidden in hide):
        up()
        goto(0, 0)
        color('white')
        write("¡Juego completado!", align="center", font=('Arial', 30, 'bold'))
    
    update()
    ontimer(draw, 100)

shuffle(tiles)
setup(420, 420, 370, 0)
addshape(car)
hideturtle()
tracer(False)
onscreenclick(tap)
draw()
done()
