# ************************************

# Python Snake

# ************************************

from tkinter import *
import random



GAME_WIDTH = 700
GAME_HEIGHT = 700
SPEED = 800
SPACE_SIZE = 50
BODY_PARTS = 3
SNAKE_COLOR = "#00FF00"
FOOD_COLOR = "#FF0000"
BACKGROUND_COLOR = "#000000"
linked_list = [-10, 61, 199]

class Snake:
    def __init__(self):
        self.body_size = BODY_PARTS
        self.coordinates = []
        self.squares = []
        self.texts = [] # the values in the linked list

        for i in range(0, BODY_PARTS):
            self.coordinates.append([0, 0])
        i = 0
        for x, y in self.coordinates:
            circle = canvas.create_oval(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=SNAKE_COLOR, tag="snake")
            self.squares.append(circle)
            node_val = canvas.create_text((x + x + SPACE_SIZE)/2, (y + y + SPACE_SIZE)/2, text=str(linked_list[i]), font=('Helvetica 15 bold'), tag="node_val")
            self.texts.append(node_val)
            i += 1     

class Food:
    def __init__(self):
        # makes a new food with random value at random coordinate on screen
        x = random.randint(0, (GAME_WIDTH / SPACE_SIZE)-1) * SPACE_SIZE
        y = random.randint(0, (GAME_HEIGHT / SPACE_SIZE) - 1) * SPACE_SIZE
        self.coordinates = [x, y]
        to_add = random.randint(-1000, 1000)
        self.food_text = to_add
        canvas.create_oval(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=FOOD_COLOR, tag="food")
        canvas.create_text((x+x+SPACE_SIZE)/2,(y+y+SPACE_SIZE)/2,text=str(to_add),font=('Helvetica 15 bold'), tag="food_text")

def next_turn(snake, food):
    print('next turn')

    # calculating new coordinates - will stay if food not hit
    x, y = snake.coordinates[0]
    case = -1
    if direction == "up":
        y -= SPACE_SIZE
        case = 1
    elif direction == "down":
        y += SPACE_SIZE
        case = 2
    elif direction == "left":
        x -= SPACE_SIZE
        case = 3
    elif direction == "right":
        x += SPACE_SIZE
        case = 4
    
    # creating new node - will stay if food not hit
    snake.coordinates.insert(0, (x, y))
    circle = canvas.create_oval(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=SNAKE_COLOR)
    snake.squares.insert(0, circle)

    # rerender the linked list
    if not(x == food.coordinates[0] and y == food.coordinates[1]):
        canvas.delete("node_val")
        snake.texts = []
        print(linked_list)
        for i in range(len(linked_list)):
            a, b = snake.coordinates[i]
            node_val = canvas.create_text((a+a+SPACE_SIZE)/2,(b+b+SPACE_SIZE)/2,font=('Helvetica 15 bold'), text=str(linked_list[i]),tag="node_val")
            snake.texts.append(node_val)
    
    # manually add the text of the last node
    node_vall = canvas.create_text((x+x+SPACE_SIZE)/2,(y+y+SPACE_SIZE)/2,font=('Helvetica 15 bold'), text=str(linked_list[len(linked_list)-1]),tag="node_val")
    snake.texts.append(node_vall)

    # ate the food
    if x == food.coordinates[0] and y == food.coordinates[1]:
        global score
        score += 1
        label.config(text="Score:{}".format(score))
        canvas.delete("food")
        canvas.delete("food_text")
        linked_list.append(food.food_text)
        linked_list.sort()
        snake.texts = []
        canvas.delete("node_val")

        # rerender the list to include the new value
        for i in range(len(linked_list)):
            a, b = snake.coordinates[i]
            node_val = canvas.create_text((a+a+SPACE_SIZE)/2,(b+b+SPACE_SIZE)/2,font=('Helvetica 15 bold'),text=str(linked_list[i]),tag="node_val")
            snake.texts.append(node_val)
        food = Food()
    else:
        del snake.coordinates[-1]
        canvas.delete(snake.squares[-1])
        canvas.delete(snake.texts[-1])
        del snake.squares[-1]
        del snake.texts[-1]
    if check_collisions(snake):
        game_over()
    else:
        window.after(SPEED, next_turn, snake, food)

def change_direction(new_direction):
    global direction
    if new_direction == 'left':
        if direction != 'right':
            direction = new_direction
    elif new_direction == 'right':
        if direction != 'left':
            direction = new_direction
    elif new_direction == 'up':
        if direction != 'down':
            direction = new_direction
    elif new_direction == 'down':
        if direction != 'up':
            direction = new_direction

def check_collisions(snake):
    x, y = snake.coordinates[0]
    if x < 0 or x >= GAME_WIDTH:
        return True
    elif y < 0 or y >= GAME_HEIGHT:
        return True
    for body_part in snake.coordinates[1:]:
        if x == body_part[0] and y == body_part[1]:
            return True
    return False

def game_over():
    canvas.delete(ALL)
    canvas.create_text(canvas.winfo_width()/2, canvas.winfo_height()/2,
                       font=('consolas',70), text="GAME OVER", fill="red", tag="gameover")

window = Tk()
window.title("Snake game")
window.resizable(False, False)
score = 0
direction = 'down'
label = Label(window, text="Score:{}".format(score), font=('consolas', 40))
label.pack()
canvas = Canvas(window, bg=BACKGROUND_COLOR, height=GAME_HEIGHT, width=GAME_WIDTH)
canvas.pack()
window.update()

window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
x = int((screen_width/2) - (window_width/2))
y = int((screen_height/2) - (window_height/2))
window.geometry(f"{window_width}x{window_height}+{x}+{y}")
window.bind('<Left>', lambda event: change_direction('left'))
window.bind('<Right>', lambda event: change_direction('right'))
window.bind('<Up>', lambda event: change_direction('up'))
window.bind('<Down>', lambda event: change_direction('down'))

snake = Snake()
food = Food()

next_turn(snake, food)
window.mainloop()

