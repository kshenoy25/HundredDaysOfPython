from turtle import Turtle, Screen

# python higher order function and event listener
tim = Turtle()
screen = Screen()

def move_forward():
    tim.forward(10)

def move_backward():
    tim.backward(10)

def turn_left():
    #tim.left(10)
    new_heading = tim.heading() + 10
    tim.setheading(new_heading)

def turn_right():
    #tim.right(10)
    new_heading = tim.heading() - 10
    tim.setheading(new_heading)

def clear():
    tim.clear()
    tim.penup()
    # brings back turtle back to the original position
    tim.home()
    tim.pendown()

screen.listen()
#screen.onkey(key="space", fun=move_forward)
screen.onkey(move_forward, "w")
screen.onkey(move_backward, "s")
screen.onkey(turn_left, "a")
screen.onkey(turn_right, "d")
screen.onkey(clear, "c")
screen.exitonclick()