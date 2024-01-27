from turtle import Turtle

ALIGMENT = "center"
FONT = ("Courier", 40, "normal")


class Scoreboard(Turtle):

  def __init__(self):
    super().__init__()
    self.score_right = 0
    self.score_left = 0
    self.color("white")
    self.penup()
    self.goto(0, 240)
    self.hideturtle()
    self.update_scoreboard()

  def update_scoreboard(self):
    self.write(f"{self.score_left}   |   {self.score_right}",
               align=ALIGMENT,
               font=FONT)

  def game_over(self):
    self.goto(0, 0)
    if self.score_left > self.score_right:
      self.write("Left user wins", align=ALIGMENT, font=FONT)
    else:
      self.write("Right user wins", align=ALIGMENT, font=FONT)

  def increase_score_left(self):
    self.score_left += 1
    self.clear()
    self.update_scoreboard()

  def increase_score_right(self):
    self.score_right += 1
    self.clear()
    self.update_scoreboard()