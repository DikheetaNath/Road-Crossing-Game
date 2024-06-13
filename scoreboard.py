from turtle import Turtle


class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.score = 0
        self.goto(-280, 280)
        self.write('Score : 0', align='center',  font=('classic', 20, 'normal'))

    def update_score(self):
        self.score += 1
        self.clear()
        self.write(f'Score : {self.score}', align='center',  font=('classic', 20, 'normal'))
