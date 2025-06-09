from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.shape("circle")
        self.speed("slowest")
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1


    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def collision_with_the_wall_y(self):
        self.y_move *= -1

    def collision_with_the_wall_x(self):
        self.x_move *= -1

    def out_of_bounds(self):
        self.move_speed = 0.1
        self.goto(0,0)
        self.x_move *= -1


