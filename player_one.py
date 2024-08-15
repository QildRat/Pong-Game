from turtle import Turtle

PADDLE_POS = [40, 20, 0, -20, -40]
LEFT_PADDLE_POS = -380


class Paddle(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.paddle_y_pos = PADDLE_POS
        self.paddle_x_pos = LEFT_PADDLE_POS
        self.segment_list = []
        self.create_paddle()

    def create_paddle(self):
        for position in self.paddle_y_pos:
            new_segment = Turtle("square")
            new_segment.color("white")
            new_segment.teleport(x=self.paddle_x_pos, y=position)
            self.segment_list.append(new_segment)

    def up(self):
        for segments in self.segment_list:
            segments.penup()
            segments.setheading(90)
            segments.forward(30)

    def down(self):
        for segments in self.segment_list[::-1]:
            segments.penup()
            segments.setheading(270)
            segments.forward(30)
