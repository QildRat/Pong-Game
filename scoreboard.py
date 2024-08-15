from turtle import Turtle

FONT = ("Goudy Old Style", 40, 'normal')


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.player1_score = 0
        self.player2_score = 0
        self.display_score()

    def display_score(self):
        self.hideturtle()
        self.color("white")
        self.penup()
        self.teleport(x=0, y=240)
        self.write(f"{self.player1_score}    {self.player2_score}", True, align="center", font=FONT)

    def update_score(self):
        self.clear()
        self.display_score()

    def game_over(self):
        self.hideturtle()
        self.color("white")
        self.penup()
        self.home()
        self.write("GAME OVER!", True, align="center", font=FONT)
