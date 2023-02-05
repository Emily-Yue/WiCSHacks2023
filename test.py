# ************************************
# Python Snake
# ************************************

from tkinter import *
import random
import sys

GAME_WIDTH = 700
GAME_HEIGHT = 700
LISTPANE_WIDTH = 900
LISTPANE_HEIGHT = 300
SPEED = 400
SPACE_SIZE = 50
BODY_PARTS = 3
SNAKE_COLOR = "#00FF00"
FOOD_COLOR = "#FF0000"
BACKGROUND_COLOR = "#000000"
linked_list = []
NODE_LENGTH = 100
NODE_Y1 = 50
NODE_Y2 = 150
FIRST_VAL = -1001
SECOND_VAL = -1002
THIRD_VAL = -1003
first_time = True

class Snake:
    def __init__(self):
        self.body_size = BODY_PARTS
        self.coordinates = []
        self.circles = []

        for i in range(0, BODY_PARTS):
            self.coordinates.append([0, 0])

        for x, y in self.coordinates:
            to_add = random.randint(-1000, 1000)
            linked_list.append(to_add)
            print(linked_list)
            circle = canvas.create_oval(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=SNAKE_COLOR, tag="snake")
            self.circles.append(circle)





class Food:
    def __init__(self):
        x = random.randint(0, (GAME_WIDTH / SPACE_SIZE)-1) * SPACE_SIZE
        y = random.randint(0, (GAME_HEIGHT / SPACE_SIZE) - 1) * SPACE_SIZE
        self.coordinates = [x, y]
        to_add = random.randint(-1000, 1000)
        # linked_list.append(to_add)
        # print(linked_list)
        canvas.create_oval(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=FOOD_COLOR, tag="food")
        canvas.create_text((x+x+SPACE_SIZE)/2,(y+y+SPACE_SIZE)/2,text=str(to_add))

def next_turn(snake, food):
    x, y = snake.coordinates[0]
    if direction == "up":
        y -= SPACE_SIZE
    elif direction == "down":
        y += SPACE_SIZE
    elif direction == "left":
        x -= SPACE_SIZE
    elif direction == "right":
        x += SPACE_SIZE
    
    snake.coordinates.insert(0, (x, y))
    if first_time:
        to_add = random.randint(-1000, 1000)
        linked_list.append(to_add)
        print(linked_list)
        circle = canvas.create_oval(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=SNAKE_COLOR)
        canvas.create_text((x+x+SPACE_SIZE)/2,(y+y+SPACE_SIZE)/2,text=str(to_add))
        first_time = False
    else:
        circle = canvas.create_oval(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=SNAKE_COLOR)
        # canvas.create_text((x+x+SPACE_SIZE)/2,(y+y+SPACE_SIZE)/2,text=str(to_add))
    snake.circles.insert(0, circle)
    if x == snake.coordinates[0] and y == snake.coordinates[1]:
        global score
        score += 1  
        to_add = random.randint(-1000, 1000)
        linked_list.append(to_add)      
        label.config(text="Score:{}".format(score))
        canvas.delete("food")
        food = Food()
    else:
        del snake.coordinates[-1]
        canvas.delete(snake.circles[-1])
        del snake.circles[-1]

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

def run():
    win = Tk()
    win.state('zoomed')
    win.title('A title')

    FH = 100  # Footer height
    header_width = win.winfo_screenwidth()
    footer_width = win.winfo_screenwidth()

    footer_height = FH
    header_height = win.winfo_screenheight() - FH

    split = header_height / win.winfo_screenheight() # How much header occupies.

    header = Canvas(win, bg='#808080', borderwidth=0, highlightthickness=0,
                    width=header_width, height=header_height)
    header.place(rely=0, relheight=split, relwidth=1, anchor=N,
                 width=header_width, height=header_height)

    footer = Canvas(win, bg='#A5A5A5', borderwidth=2, highlightthickness=0,
                    width=footer_width, height=footer_height)

    footer.place(rely=split, relheight=1.0-split, relwidth=1, anchor=N,
                 width=footer_width, height=footer_height)

    if __name__ == '__main__':
        win.mainloop()    

# def list_window_stuff(win):
#     ttk.Button(win, "Confirm", font=('Aerial 17 bold italic')).pack(pady=)

def game_over():
    canvas.delete(ALL)
    canvas.create_text(canvas.winfo_width()/2, canvas.winfo_height()/2,
                       font=('consolas',70), text="GAME OVER", fill="red", tag="gameover")

    # snake = Snake()
    # food = Food()
    # next_turn(snake, food)
    # window.mainloop()

# sys.setrecursionlimit(20000)

# def draw_draggable_nodes():

window = Tk()
window2 = Tk()
window.title("Snake game")
window.resizable(False, False)
window2.resizable(False, False)
score = 0
direction = 'down'

label = Label(window, text="Score:{}".format(score), font=('consolas', 40))
label.pack()
canvas = Canvas(window, bg=BACKGROUND_COLOR, height=GAME_HEIGHT, width=GAME_WIDTH)
canvas2 = Canvas(window2, bg=BACKGROUND_COLOR, height=LISTPANE_HEIGHT, width=LISTPANE_WIDTH)
canvas.pack()
canvas2.pack()
window.update()
window2.update()

# run()

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

# determine math stuff and increments
empty = (LISTPANE_WIDTH - 3*NODE_LENGTH)/4
first_x1 = empty
first_x2 = first_x1 + NODE_LENGTH
second_x1 = first_x2 + empty
second_x2 = second_x1 + NODE_LENGTH
third_x1 = second_x2 + empty
third_x2 = third_x1 + NODE_LENGTH
print("HEY ",linked_list)
canvas2.create_oval(first_x1, NODE_Y2, first_x2, NODE_Y1, width='2', outline='white')
canvas2.create_text((first_x1+first_x2)/2, (NODE_Y1+NODE_Y2)/2, text=str(linked_list[0]))
canvas2.create_oval(second_x1, NODE_Y2, second_x2, NODE_Y1, width='2', outline='white')
# canvas2.create_text((second_x1+second_x2)/2, (NODE_Y1+NODE_Y2)/2, text=str(linked_list[1]))
canvas2.create_oval(third_x1, NODE_Y2, third_x2, NODE_Y1, width='2', outline='white')
# canvas2.create_text((third_x1+third_x2)/2, (NODE_Y1+NODE_Y2)/2, text=str(linked_list[2]))

next_turn(snake, food)
window.mainloop()
window2.mainloop()

# from tkinter import *
# class CanvasDemo(Frame):
#     def __init__(self, width=200, height=200):
#         Frame.__init__(self, root)
#         self.canvas = Canvas(self)
#         self.canvas.pack(fill="both", expand="1")
#         self.canvas.create_rectangle(50, 25, 150, 75, fill="bisque", tags="r1")
#         self.canvas.create_line(0,0, 50, 25, arrow="last", tags="to_r1")
#         self.canvas.bind("<B1-Motion>", self.move_box)
#         self.canvas.bind("<ButtonPress-1>", self.start_move)

#     def move_box(self, event):
#         deltax = event.x - self.x
#         deltay = event.y - self.y
#         self.canvas.move("r1", deltax, deltay)
#         coords = self.canvas.coords("to_r1")
#         coords[2] += deltax
#         coords[3] += deltay
#         self.canvas.coords("to_r1", *coords)
#         self.x = event.x
#         self.y = event.y

#     def start_move(self, event):
#         self.x = event.x
#         self.y = event.y

# root = Tk()
# canvas = CanvasDemo(root)
# canvas.pack()
# mainloop()