from turtle import Screen
from snake import Snake
from food import Food
from score import Scoreboard
import time

screen = Screen()

screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('Snake Game')
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()
screen.listen()
screen.onkey(snake.up, 'Up')
screen.onkey(snake.down, 'Down')
screen.onkey(snake.left, 'Left')
screen.onkey(snake.right, 'Right')

gameIsOn = True

while gameIsOn:
    screen.update()
    time.sleep(0.15)
    snake.snake_movement()

    if snake.head.distance(food) < 15:
        food.location()
        snake.snake_grow()
        scoreboard.increase_score()

    for part in snake.snakeParts[1:]:
        if snake.head.distance(part) < 10:
            scoreboard.reset()
            snake.reset_snake()

    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        scoreboard.reset()
        snake.reset_snake()


screen.exitonclick()
