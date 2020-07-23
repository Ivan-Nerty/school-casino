import turtle
import random

coin=[]

def CoinCreate():
    for i in range(10):
        print(len(coin))
        coin.append(turtle.Turtle())
        coin[len(coin)-1].shape("coin.gif")
        coin[len(coin)-1].penup()
        coin[len(coin)-1].hideturtle()
        coin[len(coin)-1].setpos(random.randint(-350,-250),260)
        coin[len(coin)-1].showturtle()
        turtle.delay(15)
        turtle.speed(8)
        coin[len(coin)-1].right(90)
        coin[len(coin)-1].forward(500)

def CoinCreate2():
    for i in range(5):
        print(len(coin))
        coin.append(turtle.Turtle())
        coin[len(coin)-1].shape("coin.gif")
        coin[len(coin)-1].penup()
        coin[len(coin)-1].hideturtle()
        coin[len(coin)-1].setpos(random.randint(-350,-250),260)
        coin[len(coin)-1].showturtle()
        turtle.delay(15)
        turtle.speed(8)
        coin[len(coin)-1].right(90)
        coin[len(coin)-1].forward(500)

def Click(x,y):
    global Round
    print(len(coin))
    turtle.delay(15)
    turtle.speed(3)
    coin[len(coin)-1].setpos(-85,-190)
    coin[len(coin)-1].hideturtle()
    del(coin[len(coin)-1])
    t_knob.setpos(213,-90)
    t_knob.setpos(213,120)
    Round=0

turtle.setup(800,600)

turtle.speed(0)
turtle.delay(0)

turtle.hideturtle()

turtle.addshape("1.gif")
turtle.addshape("2.gif")
turtle.addshape("3.gif")
turtle.addshape("4.gif")
turtle.addshape("a.gif")
turtle.addshape("b.gif")
turtle.addshape("coin.gif")

t_background=turtle.Turtle()
t_knob=turtle.Turtle()

t_background.shape("a.gif")
t_knob.shape("b.gif")

t_knob.setpos(213,120)

t_fruit1=turtle.Turtle()
t_fruit2=turtle.Turtle()
t_fruit3=turtle.Turtle()

t1=0
t2=0
t3=0

turtle.delay(0)

#1
t_fruit1.hideturtle()
t_fruit1.penup()
turtle.speed(0)
f1=random.randint(1,3)

if f1 == 1:
    t_fruit1.shape("1.gif")
if f1 == 2:
    t_fruit1.shape("2.gif")
if f1 == 3:
    t_fruit1.shape("4.gif")

t_fruit1.setpos(-15,50)
t_fruit1.showturtle()
#2
t_fruit2.hideturtle()
t_fruit2.penup()
turtle.speed(0)
f2=random.randint(1,3)

if f2 == 1:
    t_fruit2.shape("1.gif")
if f2 == 2:
    t_fruit2.shape("2.gif")
if f2 == 3:
    t_fruit2.shape("4.gif")

t_fruit2.setpos(-135,50)
t_fruit2.showturtle()
#3
t_fruit3.hideturtle()
t_fruit3.penup()
turtle.speed(0)
f3=random.randint(1,3)

if f3 == 1:
    t_fruit3.shape("1.gif")
if f3 == 2:
    t_fruit3.shape("2.gif")
if f3 == 3:
    t_fruit3.shape("4.gif")

t_fruit3.setpos(110,50)
t_fruit3.showturtle()

CoinCreate2()

Round=0
while True:
    turtle.delay(30)
    if Round < 90:
        Round=Round+1

    if Round < 30:
        f1=random.randint(1,3)
        if f1 == 1:
            t_fruit1.shape("1.gif")
        if f1 == 2:
            t_fruit1.shape("2.gif")
        if f1 == 3:
            t_fruit1.shape("4.gif")

    if Round < 60:
        f2=random.randint(1,3)
        if f2 == 1:
            t_fruit2.shape("1.gif")
        if f2 == 2:
            t_fruit2.shape("2.gif")
        if f2 == 3:
            t_fruit2.shape("4.gif")

    if Round < 90:
        f3=random.randint(1,3)
        if f3 == 1:
            t_fruit3.shape("1.gif")
        if f3 == 2:
            t_fruit3.shape("2.gif")
        if f3 == 3:
            t_fruit3.shape("4.gif")

    if Round == 90:
        Round=Round+1
        if (f1 == f2) and (f2 == f3):
            CoinCreate()
        if (f1 == f2) or (f1 == f3) or (f2 == f3):
            CoinCreate2()

    if Round == 91:
        t_knob.onclick(Click)

turtle.done()