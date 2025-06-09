from turtle import Turtle, Screen

class Paddle(Turtle):
    def __init__(self, tuple):
        super().__init__()
        self.penup()
        self.tuple = tuple
        self.color("white")
        self.shape("square")
        self.speed("fastest")
        self.goto(self.tuple)
        self.shapesize(stretch_wid=5, stretch_len=1)
    
    def move_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)
    
    def move_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)

    