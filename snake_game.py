from turtle import Screen, Turtle
from snake import Snake
from scoreboard import Scoreboard
import time
from food import Food

screen= Screen()
screen.setup(width=600,height=600)
screen.bgcolor('black')
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()

score = Scoreboard()
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on =True

while game_is_on:
    screen.update()
    time.sleep(0.09)
    snake.move()

    if snake.head.distance(food)< 15:
        print('nom nom nom')
        food.refresh()
        snake.extend_segments()
        score.increase_score()

    if snake.head.xcor()>280 or snake.head.xcor()<-280 or snake.head.ycor()>280 or snake.head.ycor()<-280:
        score.reset()
        snake.reset()

    for segment in snake.segments:
        if segment == snake.head:
            pass
        elif snake.head.distance(segment) <10:
            score.reset()
            snake.reset()



screen.exitonclick()