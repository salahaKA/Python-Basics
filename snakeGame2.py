import turtle
import time
import random
delay= 0.1

#Score
score= 0.1
high_score= 0


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
#Pen
pen= turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("black")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Score: 0, High Score:0", align="center", font=("courier",24, "normal"))

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
        segments.clear()

        #Reset score
        score=0
        #Reset delay
        delay= 0.1
        pen.clear()
        pen.write("score: {} High Score: {}".format(score,high_score),align="center" ,font=("Courier",24, "normal"))




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
        new_segment.color("grey")
        new_segment.penup()
        segments.append(new_segment)


        #Shorten delay
        delay-= 0.001
        #Increase score
        score+= 10
        if score> high_score:
            high_score= score
        pen.clear()
        pen.write("score: {} High Score: {}".format(score,high_score),align="center" ,font=("Courier",24, "normal"))

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

            #Reset score
            score=0

            #Reset delay
            delay= 0.1

            #Update score display
            pen.clear()
            pen.write("score: {} High Score: {}".format(score,high_score),align="center" ,font=("Courier",24, "normal"))


    time.sleep(delay)

wn.mainloop()
