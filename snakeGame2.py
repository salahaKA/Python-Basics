import turtle
import time
import random
delay= 0.1

#setup screen
wn= turtle.Screen()
wn.title("Snake game by Salaha")
wn.bgcolor("yellow")
wn.setup(width=600, height=600)
wn.tracer(0)  

#snake head
head= turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("black")
head.penup()
head.goto(0,0) #center
head.direction= 'stop'

#Snake Food
food= turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(0,100) #center

segments= []
# Functions

def go_up():
    if head.direction != 'down':
        head.direction= 'up'
def go_down():
    if head.direction != 'up':
        head.direction= 'down'
def go_left():
    if head.direction != 'right':
        head.direction= 'left'
def go_right():
    if head.direction != 'left':
        head.direction= 'right'

def move():
    if head.direction== "up":
        y= head.ycor()
        head.sety(y+ 20)

    if head.direction== "down":
        y= head.ycor()
        head.sety(y- 20)

    if head.direction== "left":
        x= head.xcor()
        head.setx(x- 20)

    if head.direction== "right":
        x= head.xcor()
        head.setx(x+ 20)

#Keyboard bindings
wn.listen()
wn.onkey(go_up, "Up")
wn.onkey(go_down, "Down")
wn.onkey(go_left, "Left")
wn.onkey(go_right, "Right")

#Main game loop
while True:
    wn.update()
    #check for collition with border
    if head.xcor()>290 or head.xcor()<-290 or head.ycor()>290 or head.ycor()<-290:
        time.sleep(1)
        head.goto(0,0)
        head.direction= 'stop'

        #Hidethe segments
        for segment in segments:
            segment.goto(1000,1000)
        #clear segment list
        segment.clear()



    #check for collition with food

    if head.distance(food)< 20:
        #Move the food to random position
        x= random.randint(-290, 290)
        y= random.randint(-290, 290)
        food.goto(x,y)

        #Add a segment
        new_segment= turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("gray")
        new_segment.penup()
        segments.append(new_segment)

    #move the end seg first
    for index in range(len(segments)-1, 0, -1):
        x= segments[index-1].xcor()
        y= segments[index-1].ycor()
        segments[index].goto(x,y)
    #Move segment 0 where the head is
    if len(segments)>0:
        x=head.xcor()
        y=head.ycor()
        segments[0].goto(x,y)


    move()

    #check for head collition wuth body
    for segment in segments:
        if segment.distance(head)<20:
            time.sleep(1)
            head.goto(0,0)
            head.direction= 'stop'

            #Hidethe segments
            for segment in segments:
                segment.goto(1000,1000)
            #clear segment list
            segment.clear()

    time.sleep(delay)

wn.mainloop()
