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
player_one.penup() # clean line
player_one.goto(-350, 0)
player_one.shapesize(stretch_wid=3, stretch_len=1)

# PLAYER TWO
player_two = turtle.Turtle()
player_two.speed(0)
player_two.shape('square')
player_two.color('white')
player_two.penup() # clean line
player_two.goto(350, 0)
player_two.shapesize(stretch_wid=5, stretch_len=1)

# BALL
ball = turtle.Turtle()
ball.speed(0)
ball.shape('square')
ball.color('white')
ball.penup() # clean line
ball.goto(0, 0)

# LINE
line = turtle.Turtle()
line.color('white')
line.goto(0, -400)
line.goto(0, 400)

while True:
  window.update()