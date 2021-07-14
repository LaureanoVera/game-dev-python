import turtle

# WINDOW
window = turtle.Screen()
window.title('Pong Game')
window.bgcolor('black')
window.setup(width=800, height=600)
window.tracer(0)

# PLAYER ONE
player_one = turtle.Turtle()
player_one.speed(0)
player_one.shape('square')
player_one.color('white')
player_one.penup()  # clean line
player_one.goto(-350, 0)
player_one.shapesize(stretch_wid=5, stretch_len=1)

# PLAYER TWO
player_two = turtle.Turtle()
player_two.speed(0)
player_two.shape('square')
player_two.color('white')
player_two.penup()  # clean line
player_two.goto(350, 0)
player_two.shapesize(stretch_wid=5, stretch_len=1)

# BALL
ball = turtle.Turtle()
ball.speed(0)
ball.shape('square')
ball.color('white')
ball.penup()  # clean line
ball.goto(0, 0)
ball.dx = 1
ball.dy = 1

# LINE
line = turtle.Turtle()
line.color('white')
line.goto(0, -400)
line.goto(0, 400)

# FUNCTIONS


def player_one_up():
    y = player_one.ycor()
    y += 30
    player_one.sety(y)


def player_one_down():
    y = player_one.ycor()
    y -= 30
    player_one.sety(y)


def player_two_up():
    y = player_two.ycor()
    y += 30
    player_two.sety(y)


def player_two_down():
    y = player_two.ycor()
    y -= 30
    player_two.sety(y)


# KEYS
window.listen()
window.onkeypress(player_one_up, 'w')
window.onkeypress(player_one_down, 's')
window.onkeypress(player_two_up, 'Up')
window.onkeypress(player_two_down, 'Down')

while True:
    window.update()

    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # BORDER
    if ball.ycor() > 290:
        ball.dy *= -1

    if ball.ycor() < -290:
        ball.dy *= -1

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1

    if ((ball.xcor() > 340 and ball.xcor() < 350) and
        (ball.ycor() < player_two.ycor() + 50) and
        (ball.ycor() > player_two.ycor() - 50)):
      ball.dx *= -1

    if ((ball.xcor() < -340 and ball.xcor() > -350) and
        (ball.ycor() < player_one.ycor() + 50) and
        (ball.ycor() > player_one.ycor() - 50)):
      ball.dx *= -1
