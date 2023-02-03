# made by Jayavant 

from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()

screen.setup(600, 600)

screen.bgcolor("black")
screen.title("Snake Game by Jayavant")
screen.tracer(0)
snake = Snake()
food = Food()
score = Scoreboard()

screen.listen()
screen.onkey(snake.move_up, "Up")
screen.onkey(snake.move_down, "Down")
screen.onkey(snake.move_right, "Right")
screen.onkey(snake.move_left, "Left")

snake_on = True

while snake_on:
    snake.move()
    screen.update()
    time.sleep(0.2)

    # collision with food
    if snake.head.distance(food) < 15:
        snake.extend()
        food.refresh()
        score.increase_score()


    #DETECT COLLISION WITH WALL

    if snake.head.xcor() < -280 or snake.head.xcor() > 280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        snake_on = False
        score.game_over()

    # detect collision with tail

    for segment in snake.segments[1:]:

        if snake.head.distance(segment) < 10:
            snake_on = False
            score.game_over()

screen.exitonclick()
