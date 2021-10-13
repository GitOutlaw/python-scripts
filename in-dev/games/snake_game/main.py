from turtle import Screen
import time
from food import Food
from snake import Snake
from scoreboard import Scoreboard

# Setup the screen.
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

# Instantiate snake, food & scoreboard.
snake = Snake()
food = Food()
scoreboard = Scoreboard()

# Setup the controls of game.
screen.listen()
screen.onkeypress(snake.up, "Up")
screen.onkeypress(snake.down, "Down")
screen.onkeypress(snake.left, "Left")
screen.onkeypress(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Detect collision with food and refreshes food location.
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    # Detect collison with wall.
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on = False
        scoreboard.game_over()

    # Detect collison with tail.
    for segement in snake.segments[1:]:     
        if snake.head.distance(segement) < 10:
            game_is_on = False
            scoreboard.game_over()


screen.exitonclick()
