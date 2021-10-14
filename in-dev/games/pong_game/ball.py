from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1

    def move(self):
        '''Moves the ball.'''
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        '''Bounces the ball on y axis.'''
        self.y_move *= -1

    def bounce_x(self):
        '''Bounces the ball on the x axis.'''
        self.x_move *= -1
        self.move_speed *= 0.9

    def reset_position(self):
        ''''Resets the balls position when point is scored.'''
        self.goto(0, 0)
        self.move_speed = 0.1
        self.bounce_x()
