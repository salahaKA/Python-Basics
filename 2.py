# from turtle import Turtle,Screen
# tim= Turtle()
# my_screen= Screen()
# tim.shape("turtle")
# tim.color("red")
# #tim.forward(100)
# #tim.circle(50)
# tim.left(90)
# tim.circle(100)
# tim.speed(0)
# my_screen.exitonclick()
#---------------------------

# from turtle import Turtle,Screen
# tim= Turtle()
# my_screen= Screen()
# tim.shape("turtle")
# tim.color("red")
# tim.speed(0)
# for i in range(180):
#     tim.circle(100)
#     tim.left(2)
# my_screen.exitonclick()

#----------------------------------
import random
from turtle import Turtle,Screen
tim= Turtle()
my_screen= Screen()
colors= ["red", "green", "blue", "black", "pink", "orange", "violet"]
tim.speed(0)
for i in range(180):
    a=  random.randint(0,6)
    tim.color(colors[a])
    tim.circle(100)
    tim.left(2)
my_screen.exitonclick()

#-----------------------------------------