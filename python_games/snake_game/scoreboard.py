from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color('white')
        self.penup()
        self.goto(0,270)
        self.write(f'Score: {self.score}', False, align='Center', font=('Arial',16,'bold'))
        self.hideturtle() # Så ingen pil syns

    def update_scoreboard(self):
        self.write(f'Score: {self.score}', False, align='Center', font=('Arial', 16, 'bold'))


    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()
