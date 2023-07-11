from turtle import Turtle

FONT = ("Ariel", 8, "normal")
ALIGNMENT = "center"


class DrawState(Turtle):

    def __init__(self):
        super(DrawState, self).__init__()
        self.hideturtle()
        self.penup()
        self.speed(0)

    def write_state(self, x, y, state):
        self.goto(x, y)
        self.write(f"{state}", align=ALIGNMENT, font=FONT)
