from turtle import Turtle, Screen
import random


screen=Screen()
screen.setup(500,400)
input=screen.textinput(title="Make a bet", prompt="Which turtle will win the race? Enter the colour from: red, blue, orange, purple, green or yellow ")
colors=["red","blue", "orange", "purple", "green","yellow"]
y_position=[-60,-30,0, 30,60,90]
all_turtle=[]
is_race_on= False

for i in range(6):
    tim=Turtle(shape="turtle")
    tim.color(colors[i])
    tim.penup()
    tim.goto(-200,y_position[i])
    all_turtle.append(tim)

if input:
    is_race_on=True

while is_race_on:

    for turtle in all_turtle:
        if turtle.xcor() > 230:
            is_race_on=False
            winning_color=turtle.pencolor()
            if winning_color==input:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")

        rand_distance=random.randint(0,10)
        turtle.forward(rand_distance)






screen.exitonclick()
