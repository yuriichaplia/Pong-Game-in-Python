import time
from ball import Ball
from paddle import Paddle
from turtle import Screen
from scoreboard import ScoreBoard

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)

ball = Ball()
r_paddle = Paddle((350,0))
l_paddle = Paddle((-350,0))
scoreboard = ScoreBoard()

screen.listen()
screen.onkeypress(r_paddle.move_up, "Up")
screen.onkeypress(r_paddle.move_down, "Down")
screen.onkeypress(l_paddle.move_up, "w")
screen.onkeypress(l_paddle.move_down, "s")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    if ball.ycor() >= 280 or ball.ycor() <= -280:
        ball.collision_with_the_wall_y()

    if ball.distance(r_paddle) < 50 and ball.xcor() > 330 or ball.distance(l_paddle) < 50 and ball.xcor() < -330:
        ball.collision_with_the_wall_x()
        ball.move_speed /= 1.1

    if ball.xcor() > 400:
        ball.out_of_bounds()
        scoreboard.l_point()

    if ball.xcor() < -400:
        ball.out_of_bounds()
        scoreboard.r_point()

screen.exitonclick()
