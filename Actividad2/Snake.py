"""Snake, classic arcade game.

Ejericicios

1. La comida podrá moverse al azar un paso a la vez y no deberá de salirse de la ventana
2. Cada vez que se corra el juego, la víbora deberá tener colores diferentes, al azar, de una serie de 5 diferentes colores, excepto el rojo.
3. Cada vez que se corra el juego, la comida deberá tener colores diferentes, al azar, de una serie de 5 diferentes colores, excepto el rojo.
"""
from random import randrange, choice
from turtle import *
from freegames import square, vector

food = vector(0, 0)
snake = [vector(10, 0)]
aim = vector(0, -10)

colors = ['blue', 'green', 'yellow', 'purple', 'orange']
snake_color = choice(colors)
food_color = choice(colors)

def change(x, y):
    """Change snake direction."""
    aim.x = x
    aim.y = y

def inside(head):
    """Return True if head inside boundaries."""
    return -200 < head.x < 190 and -200 < head.y < 190

def move():
    """Move snake forward one segment."""
    head = snake[-1].copy()
    head.move(aim)

    if not inside(head) or head in snake:
        square(head.x, head.y, 9, 'red')  # La serpiente se pinta de rojo si choca
        update()
        return

    snake.append(head)

    directions = [vector(10, 0), vector(-10, 0), vector(0, 10), vector(0, -10)]

    if head == food:
        print('Snake:', len(snake))
        # Posicionamiento aleatorio de la comida. Autor: Anhuar Maldonado 
        food.x = randrange(-15, 15) * 10
        food.y = randrange(-15, 15) * 10
    else:
        snake.pop(0)
        # Posicionamiento aleatorio de la comida. Autor: Anhuar Maldonado 
        random_direction = choice(directions)
        food.x += random_direction.x
        food.y += random_direction.y

    clear()

    # Usamos el color fijo seleccionado al inicio
    for body in snake:
        square(body.x, body.y, 9, snake_color)  # Dibuja la serpiente con el color fijo. Autor: Javier Cuatepotzo

    square(food.x, food.y, 9, food_color)  # Dibuja la comida con el color fijo. Autor: Bruno Zamora 
    update()
    ontimer(move, 100)

setup(420, 420, 370, 0)
hideturtle()
tracer(False)
listen()
onkey(lambda: change(10, 0), 'Right')
onkey(lambda: change(-10, 0), 'Left')
onkey(lambda: change(0, 10), 'Up')
onkey(lambda: change(0, -10), 'Down')
move()
done()
