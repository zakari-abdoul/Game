import turtle, os

wn = turtle.Screen()
wn.title('Ping Pong by Zakari')
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5,stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)


# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5,stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)


# Balle
Balle = turtle.Turtle()
Balle.speed(0)
Balle.shape("circle")
Balle.color("white")
Balle.shapesize(stretch_wid=1,stretch_len=1)
Balle.penup()
Balle.goto(0, 0)
Balle.dx = 0.50
Balle.dy = 0.50
#  Score
score_a = 0
score_b = 0

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Player A:0  Player B: 0 ",align="center", font=("Courier", 20, "normal"))

# Move paddles a
def paddle_a_up():
    y = paddle_a.ycor()
    y +=20
    paddle_a.sety(y)

def paddle_a_down():
    y = paddle_a.ycor()
    y -=20
    paddle_a.sety(y)


# Move paddle_b
def paddle_b_up():
    y = paddle_b.ycor()
    y +=20
    paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor()
    y -=20
    paddle_b.sety(y)

#  keyboard binding
wn.listen()

# On paddle_A
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "z")

# On paddle_b
wn.onkeypress(paddle_b_up, "p")
wn.onkeypress(paddle_b_down, "m")





# Main game loop
while True:
    wn.update()
    Balle.setx(Balle.xcor() + Balle.dx)
    Balle.sety(Balle.ycor() + Balle.dy)
    pen

    # Top Border
    if Balle.ycor() > 290:
        Balle.sety(290)
        Balle.dy = Balle.dy * -1
        os.system("aply sound.extention")

    if Balle.ycor() < -290:
        Balle.sety(-290)
        Balle.dy = Balle.dy * -1
        os.system("aply sound.extention")

    # side border
    if Balle.xcor() > 390:
        Balle.goto(0,0)
        Balle.dx = Balle.dy * -1
        score_a += 1
        pen.clear()
        pen.write("Player A:{}  Player B:{} ".format(score_a,score_b),align="center", font=("Courier", 20, "normal"))


    if Balle.xcor() < -390:
        Balle.goto(0,0)
        Balle.dx = Balle.dy * -1
        score_b += 1
        pen.clear()
        pen.write("Player A:{}  Player B:{} ".format(score_a,score_b),align="center", font=("Courier", 20, "normal"))

    
    # the ball hit the corner, his position is set to zero
    # if (Balle.xcor() > 340 and Balle.xcor() < 340):
    #     Balle.setx(0)
    #     Balle.dx *= -1
    # the balle hit the paddle

    if (Balle.xcor() > 340 and Balle.xcor() < 350) and (Balle.ycor() < paddle_b.ycor() + 40 and Balle.ycor() > paddle_b.ycor() -40):
        Balle.setx(340)
        Balle.dx *= -1

    if (Balle.xcor() < -340 and Balle.xcor() > -350) and (Balle.ycor() < paddle_a.ycor() + 40 and Balle.ycor() > paddle_a.ycor() -40):
        Balle.setx(-340)
        Balle.dx *= -1
