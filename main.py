import turtle
import random

import turtle
from turtle import color
import random

def pen(colour):
    turtle.color(colour)

def fireworks(size):
    for num in range(20):
        turtle.forward(size)
        turtle.rt(180-(360/20))

def move():
    turtle.penup()
    x=random.randint(-400,400)
    y=random.randint(-400,400)
    turtle.goto(x,y)
    turtle.pendown()

turtle.bgcolor("black")
turtle.speed(0)

colors=['red','yellow','blue','cyan','magenta','orange']
for _ in range(30):
    color=random.choice(colors)
    pen(color)
    fireworks(random.randint(50,100))
    move()
turtle.penup()
turtle.goto(-690,-100)
turtle.pendown()
turtle.color('white')
style = ('Courier', 70, 'italic bold')
turtle.write('HAPPY\nDIWALI \nTO ALL!', font=style)
turtle.hideturtle()

screen = turtle.Screen()
screen.setup(500,500)
screen.tracer(0)
screen.addshape("diya3.gif")   # register the image with the screen as a shape

don = turtle.Turtle()
screen1=turtle.clone()
screen2=turtle.clone()
screen3=turtle.clone()
don.speed(1000)
turtle.bgcolor("black")
don.shape("diya3.gif")
don.penup()

don.goto(-360,0)

while True :
    screen.update()
    don.forward(0.2)

