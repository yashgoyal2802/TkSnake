from tkinter import *
from PIL import Image, ImageTk


class Snake(Canvas):
    def __init__(self):
        super().__init__(width=600, height=620, background="black", highlightthickness=0)

        self.load_assets()

    def load_assets(self):
        try:
            # Snake image
            self.snake_body_image = Image.open("./assets/snake.png")
            self.snake_body = ImageTk.PhotoImage(self.snake_body_image)
            # Food Image
            self.food_image = Image.open("./assets/food.png")
            self.food = ImageTk.PhotoImage(self.food_image)
        except IOError as error:
            print(error)
            root.destroy()


root = Tk()
root.title("Snake Game!!")
root.resizable(False, False)    # Making it un-resizable

python = Snake()
python.pack()

root.mainloop()

