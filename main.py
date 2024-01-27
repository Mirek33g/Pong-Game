import time
from turtle import Screen
from scoreboard import Scoreboard
from ball import Ball
from paddle import Paddle

# screen setup details
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong game")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")
screen.onkey(l_paddle.up, "w")
screen.onkey(l_paddle.down, "s")

# ball speed
SPEED = 0.1

run = True
while run:
  time.sleep(SPEED)
  screen.update()
  ball.move()

  # detect colision with a wall
  if ball.ycor() > 280 or ball.ycor() < -280:
    ball.bounce_y()

# detect colision with a paddle
  elif ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(
      l_paddle) < 50 and ball.xcor() < -320:
    ball.bounce_x()
    if SPEED > 0:
      SPEED *= 0.9

  elif ball.xcor() > 400:
    scoreboard.increase_score_left()
    SPEED = 0.1
    ball.reset_position()

  elif ball.xcor() < -400:
    scoreboard.increase_score_right()
    SPEED = 0.1
    ball.reset_position()

  elif scoreboard.score_left == 10 or scoreboard.score_right == 10:
    scoreboard.game_over()
    run = False

#screen.exitonclick()