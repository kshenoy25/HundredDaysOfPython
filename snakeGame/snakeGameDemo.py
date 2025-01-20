from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

from snakeGame.scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, 'Up')
screen.onkey(snake.down, 'Down')
screen.onkey(snake.left, 'Left')
screen.onkey(snake.right, 'Right')

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    snake.move_snake()

    # detect collision with snake food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    # detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on = False
        scoreboard.game_over()

    # detect collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()


"""
segment_1 = Turtle("square")
segment_1.color("white")

segment_2 = Turtle("square")
segment_2.color("white")
segment_2.goto(-20, 0)


segment_3 = Turtle("square")
segment_3.color("white")
segment_3.goto(-40, 0)
"""
























screen.exitonclick()