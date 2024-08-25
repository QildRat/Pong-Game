from turtle import Turtle

FONT = ('Courier', 50, 'normal')


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("white")
        self.teleport(x=0, y=220)
        self.left_score = 0
        self.right_score = 0
        self.update_score()

    def display_score(self):
        """display left and right score."""
        self.write(f"{self.left_score} - {self.right_score}", False, "center", FONT)

    def update_score(self):
        """clear and redisplay the score."""
        self.clear()
        self.display_score()

    def right_add_point(self):
        self.right_score += 1

    def left_add_point(self):
        self.left_score += 1

