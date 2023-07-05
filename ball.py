from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.penup()
        self.goto(0, 0)
        self.color('GreenYellow')
        self.speed(3)
        self.extra_x = 10
        self.extra_y = 10
        self.move_speed = 0.1

    def move(self):
        self.goto(self.xcor()+self.extra_x, self.ycor() + self.extra_y)

    def bounce_y(self):
        self.extra_y *= -1
        self.move_speed *= 0.9

    def bounce_x(self):
        self.extra_x *= -1
        self.move_speed *= 0.9

    def rest_position(self):
        self.penup()
        self.goto(0, 0)
        self.bounce_x()
        self.move_speed = 0.1
