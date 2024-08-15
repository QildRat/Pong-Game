from turtle import Turtle

PADDLE_POS = [40, 20, 0, -20, -40]
LEFT_PADDLE_POS = -380
MOVE_VALUE = 60
# must match the screen width with offset of -40.
UPPER_Y = 300 - 40
LOWER_Y = (300 - 40) * -1


class Paddle(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.paddle_y_pos = PADDLE_POS
        self.paddle_x_pos = LEFT_PADDLE_POS
        self.segment_list = []
        self.create_paddle()

    def create_paddle(self):
        """make a paddle with 5 of its shape and aligned vertically on the left side of the screen."""
        for position in self.paddle_y_pos:
            new_segment = Turtle("square")
            new_segment.color("white")
            new_segment.teleport(x=self.paddle_x_pos, y=position)
            self.segment_list.append(new_segment)

    def up(self):
        """move the paddle up and forbid move if upper paddle is at the edge of screen."""
        if not self.segment_list[0].ycor() > UPPER_Y:
            for segments in self.segment_list:
                segments.penup()
                segments.setheading(90)
                segments.forward(MOVE_VALUE)

    def down(self):
        """move the paddle down and forbid move if lower paddle is at the edge of screen."""
        if not self.segment_list[-1].ycor() < LOWER_Y:
            for segments in self.segment_list[::-1]:
                segments.penup()
                segments.setheading(270)
                segments.forward(MOVE_VALUE)
