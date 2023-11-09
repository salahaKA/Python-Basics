import random
from turtle import Turtle,Screen
turtle_list= []
colors= ["red","green", "white", "yellow", "blue"]
my_screen= Screen()
my_screen.bgcolor("purple")

ycor=[0,80,160,-80,-160]
for i in range(5):
    tim= Turtle()
    tim.shape("turtle")
    tim.penup()
    tim.color(colors[i])
    tim.goto(-300,ycor[i])
    turtle_list.append(tim)

turtle_list[4].goto(300,-300)
turtle_list[4].pendown()
turtle_list[4].goto(300,300)
turtle_list[4].penup()
turtle_list[4].goto(-300,-160)

user_bet= my_screen.textinput(title="Turtle Race", prompt= "Which color turtle will win?")


w_turtle= Turtle()
w_turtle.color("red")
w_turtle.hideturtle()

for t in turtle_list:
    a= random.randint(0,25)
    t.forward(a)

game_on= True
while game_on:
    for t in turtle_list:
        a= random.randint(0,25)
        t.forward(a)
        if t.xcor()>300:
            winner= t.pencolor()
            game_on= False
            if user_bet== winner:
                w_turtle.write("You Won", font= ('Arial', '12', 'bold'))
            else:
                w_turtle.write("You loss", font= ('Arial', '12', 'bold'))


my_screen.exitonclick()