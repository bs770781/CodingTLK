from tkinter import *
import random

# Game setup
WIDTH = 400
HEIGHT = 400
SIZE = 20
speed = 100
direction = 'Right'

# Create window
win = Tk()
win.title("Simple Snake Game")
canvas = Canvas(win, width=WIDTH, height=HEIGHT, bg="black")
canvas.pack()

# Snake and food
snake = [[100, 100], [80, 100], [60, 100]]  # Starting snake
food = [random.randrange(0, WIDTH, SIZE), random.randrange(0, HEIGHT, SIZE)]
snake_blocks = []
food_block = None

def draw():
    global food_block
    canvas.delete("all")
    for x, y in snake:
        canvas.create_rectangle(x, y, x + SIZE, y + SIZE, fill="green")
    food_block = canvas.create_oval(food[0], food[1], food[0]+SIZE, food[1]+SIZE, fill="red")

def move():
    global direction, food
    head_x, head_y = snake[0]

    if direction == 'Up':
        head_y -= SIZE
    elif direction == 'Down':
        head_y += SIZE
    elif direction == 'Left':
        head_x -= SIZE
    elif direction == 'Right':
        head_x += SIZE

    new_head = [head_x, head_y]

    # Check collision
    if (new_head in snake) or head_x < 0 or head_x >= WIDTH or head_y < 0 or head_y >= HEIGHT:
        canvas.create_text(WIDTH//2, HEIGHT//2, text="Game Over", fill="white", font=('Arial', 24))
        return

    snake.insert(0, new_head)

    if new_head == food:
        food = [random.randrange(0, WIDTH, SIZE), random.randrange(0, HEIGHT, SIZE)]
    else:
        snake.pop()

    draw()
    win.after(speed, move)

def change_dir(e):
    global direction
    key = e.keysym
    opposites = {'Up':'Down', 'Down':'Up', 'Left':'Right', 'Right':'Left'}
    if key in opposites and direction != opposites[key]:
        direction = key

# Controls
win.bind('<KeyPress>', change_dir)

draw()
move()
win.mainloop()


