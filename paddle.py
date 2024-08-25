from turtle import Turtle

MOVE_VALUE = 20


class Paddle(Turtle):
    def __init__(self, x_pos, y_pos):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_len=1, stretch_wid=5)
        self.penup()
        self.teleport(x=x_pos, y=y_pos)

    def move_up(self):
        """increase value of y with the MOVE VALUE."""
        new_y = self.ycor() + MOVE_VALUE
        self.goto(x=self.xcor(), y=new_y)

    def move_down(self):
        """decrease value of y with the MOVE VALUE."""
        new_y = self.ycor() - MOVE_VALUE
        self.goto(x=self.xcor(), y=new_y)
