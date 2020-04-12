from tkinter import *
from PIL import Image, ImageTk


class Snake(Canvas):
    def __init__(self):
        super().__init__(width=600, height=620, background="black", highlightthickness=0)

        # initialising the position of food an snake
        self.snake_position = [(100, 100), (80, 100), (60, 100)]
        self.food_position = (200, 100)

        self.score = 0

        self.load_assets()
        self.create_objects()

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

    # Displaying food and snake
    def create_objects(self):
        self.create_text(
            45, 12, text=f"Score: {self.score}", tag="score", fill="#fff", font=("TkDefaultFont", 14)
        )
        for x_position, y_position in self.snake_position:
            self.create_image(x_position, y_position, image=self.snake_body, tag="snake")

        self.create_image(*self.food_position, image=self.food, tag="food")
        self.create_rectangle(7, 27, 593, 613, outline="#525d69")


root = Tk()
root.title("Snake Game!!")
root.resizable(False, False)    # Making it un-resizable

python = Snake()
python.pack()

root.mainloop()

