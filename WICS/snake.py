from tkinter import *
import random

game_width=1000
game_heights=700
speed=100
space_size=50
body_parts=3
snake_color="#00ff00"
food_color="#ff0000"
Background_color="#000000"

class snake:
    pass

class food:
    def __init__(self):
        x=random.randint(0,(game_width //space_size) -1)*snake_size 
        y=random.randint(0, (game_height // space_size) -1)*space_size
        self.coordinates=(x,y)

        canvas.create_oval(x,y,x+space_size,y+space_size,fill=food_color,tag="food")

def next_turn():
    pass

def change_direction(new direction):
    pass

def check_collision():
    pass

def game_over():
    pass


window=tk()
window.title("snake game")
window.resizable(false,false)

window.mainloop()

score=0
direction="down"
canvas=canvas(window, bg=background_color, height=game_heights, width=game_width)
canvas.pack()

window.update()

window_width=window.winfo_width()
window_height=window.winfo_height()
screen_width=window.wnfo_screenwidth()
screen_height=window.winfo_screenheight()

x=int((creen_width/2)-(window_width/2))
y=int((scree_height/2)-(window_height/2))

window.geometry(f"(window_width)x(window_height)+(x)+(y)")

snake=snake()
food=food()


window.mainloop()