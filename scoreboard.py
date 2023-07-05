from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.user_score = 0
        self.computer_score = 0
        self.update_score()

    def update_score(self):
        self.clear()
        self.goto(0, 260)
        self.write(f"user score= {self.user_score}", align="center", font=("Courier", 20, 'normal'))
        self.goto(0, 220)
        self.write(f"computer score= {self.computer_score}", align="center", font=("Courier", 20, 'normal'))

    def add_computer_score(self):
        self.computer_score += 1
        self.update_score()

    def add_user_score(self):
        self.user_score += 1
        self.update_score()

