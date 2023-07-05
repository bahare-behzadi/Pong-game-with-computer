from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, user_choice):
        super().__init__()
        self.paddle = Turtle(shape='square')
        self.paddle.penup()
        self.paddle.shapesize(stretch_wid=5, stretch_len=1)
        self.paddle.color("GreenYellow")
        self.hideturtle()
        if user_choice == "right":
            self.paddle.goto(420, 0)
        else:
            self.paddle.goto(-420, 0)
        self.paddle.speed(0)
        self.hideturtle()

    def up(self):
        self.paddle.goto(self.paddle.xcor(), self.paddle.ycor()+20)

    def down(self):
        self.paddle.goto(self.paddle.xcor(), self.paddle.ycor() - 20)
