from turtle import Turtle

# Sets constants.
ALIGNMENT = "center"
FONT = ("Courier", 24, "bold")


class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.color("white")
        self.goto(0, 265)
        self.hideturtle()
        self.update_scoreboard()

    def game_over(self):
        '''Sets the game to game over'''
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)

    def update_scoreboard(self):
        '''Updates the game scoreboard.'''
        self.write(f"Score: {self.score}", align=ALIGNMENT,
                   font=FONT)

    def increase_score(self):
        '''Sets score to + 1 when snake reaches food.'''
        self.score += 1
        self.clear()
        self.update_scoreboard()
