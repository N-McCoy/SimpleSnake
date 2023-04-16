from turtle import Turtle



class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open('data.txt') as file:
            self.highScore = int(file.read())
        self.penup()
        self.hideturtle()
        self.color('white')
        self.sety(265)
        self.update_scoreboard()

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def reset(self):
        if self.score > self.highScore:
            self.highScore = self.score
            with open('data.txt', mode='w') as file:
                file.write(str(self.highScore))

        self.score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f'Score: {self.score}   ', align='right', font=('Arial', 24, 'normal'))
        self.write(f'Highscore: {self.highScore}', align='left', font=('Arial', 24, 'normal'))

    # def game_over(self):
    #     self.setposition(0, 0)
    #     self.write('GAME OVER', align='center', font=('Arial', 30, 'normal'))