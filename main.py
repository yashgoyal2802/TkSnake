from tkinter import *


class Snake(Canvas):
    def __init__(self):
        super().__init__(width=600, height=620, background="black", highlightthickness=0)


root = Tk()
root.title("Snake Game!!")
root.resizable(False, False)    # Making it un-resizable

python = Snake()
python.pack()

root.mainloop()

