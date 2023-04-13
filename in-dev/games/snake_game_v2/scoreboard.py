from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 22, "bold")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("/media/sf_dev_share/gits/python-scripts/in-dev/games/snake_game_v2/data.txt", encoding='utf8') as data:
            self.high_score = int(data.read())
        self.color("white")
        self.penup()
        self.goto(0, 260)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        '''Updates the game scoreboard.'''
        self.clear()
        self.write(
            f"Score: {self.score} | High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def reset(self):
        '''Resets the scoreboard writing to data.txt file.'''
        if self.score > self.high_score:
            self.high_score = self.score
            with open("day24/snake_game_v2/data.txt", mode="w", encoding='utf8') as data:
                data.write(f"{self.high_score}")
        self.score = 0
        self.update_scoreboard()

    def increase_score(self):
        '''Sets score to + 1 when snake reaches food.'''
        self.score += 1
        self.update_scoreboard()
