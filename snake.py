"""Snake, classic arcade game.

Exercises

1. How do you make the snake faster or slower?
2. How can you make the snake go around the edges?
3. How would you move the food?
4. Change the snake to respond to mouse clicks.
"""

from random import randrange
from turtle import (
    update,
    ontimer,
    setup,
    hideturtle,
    tracer,
    listen,
    onkey,
    clear,
    done,
)
from freegames import square, vector

# Constants
BOUND_MIN = -200
BOUND_MAX_X = 190
BOUND_MAX_Y = 190
STEP = 10
TICK_MS = 100

# Game state
food = vector(0, 0)
snake = [vector(STEP, 0)]
aim = vector(0, -STEP)


def change(x, y):
    """Change snake direction."""
    aim.x = x
    aim.y = y


def inside(head):
    """Return True if head is inside boundaries."""
    return (
        BOUND_MIN < head.x < BOUND_MAX_X
        and BOUND_MIN < head.y < BOUND_MAX_Y
    )


def move():
    """Move snake forward one segment."""
    head = snake[-1].copy()
    head.move(aim)

    if not inside(head) or head in snake:
        square(head.x, head.y, 9, "red")
        update()
        return

    snake.append(head)

    if head == food:
        print("Snake:", len(snake))
        food.x = randrange(-15, 15) * STEP
        food.y = randrange(-15, 15) * STEP
    else:
        snake.pop(0)

    clear()

    for body in snake:
        square(body.x, body.y, 9, "black")

    square(food.x, food.y, 9, "green")
    update()
    ontimer(move, TICK_MS)


# Boot
setup(420, 420, 370, 0)
hideturtle()
tracer(False)
listen()
onkey(lambda: change(STEP, 0), "Right")
onkey(lambda: change(-STEP, 0), "Left")
onkey(lambda: change(0, STEP), "Up")
onkey(lambda: change(0, -STEP), "Down")
move()
done()
