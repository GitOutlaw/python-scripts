from turtle import Turtle

# Sets constants.
FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.penup()
        self.goto(-280, 250)
        self.write(f"Level: {self.level}", align="left", font=FONT)
        self.update_scoreboard()

    def update_scoreboard(self):
        '''Updates the game scoreboard.'''
        self.clear()
        self.write(f"Level: {self.level}", align="left", font=FONT)

    def increase_level(self):
        '''Sets score to + 1 when turtle reaches finish.'''
        self.level += 1
        self.update_scoreboard()

    def game_over(self):
        '''Sets the game to game over'''
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=FONT)
