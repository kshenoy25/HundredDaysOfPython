
####### REQUIREMENTS #######

# Create the screen
# Create and move a paddle
# Create another paddle
# Create the ball and make it move
# Detect collision with the walls and bounce
# Detect collision with the paddles
# Detect when the paddles miss
# Keep the score

from turtle import Screen, Turtle
from pong_paddle import Paddle_Left, Paddle_Right
from pong_ball import Ball
from scoreboard import Scoreboard
import time

# screen object
screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)

paddle_l = Paddle_Left()
paddle_r = Paddle_Right()
ball = Ball()
scoreboard = Scoreboard()


# moving the paddle
screen.listen()
screen.onkey(paddle_r.go_up, "Up")
screen.onkey(paddle_r.go_down, "Down")

screen.onkey(paddle_l.go_up, "w")
screen.onkey(paddle_l.go_down, "s")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    # makes sure the paddle spawns in the desired place on the screen
    screen.update()
    ball.move()

    # detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        # then the ball needs to bounce
        ball.bounce_y()

    # detect collision with paddle_r
    if ball.distance(paddle_r) < 50 and ball.xcor() > 320 or ball.distance(paddle_l) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # detect r paddle misses
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()

    # detect l paddle misses
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()




screen.exitonclick()