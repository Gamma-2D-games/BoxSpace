#Turtle Graphics Game
import turtle
import math
import random
import winsound


#screen
wn = turtle.Screen()
wn.bgcolor("black")



#draw player border
mypen = turtle.Turtle()
mypen.color("grey")
mypen.penup()
mypen.setposition(-400,-400)
mypen.pendown()
mypen.pensize(3)
for side in range(4):
    mypen.forward(800)
    mypen.left(90)
mypen.penup()


#draw goal border
mypen.color("light green")
mypen.setposition(-200, -200)
mypen.pendown()
mypen.pensize(2)
for side in range(4):
    mypen.forward(400)
    mypen.left(90)
mypen.hideturtle()

#Writing
WritePen = turtle.Turtle()
WritePen.color("pink")
WritePen.penup()
WritePen.goto(0,0)
WritePen.pendown()
WritePen.write("Gamma", False, 'center', font = ('Arial', 15, 'bold'))
WritePen.hideturtle()
               

#Create player/turtle

Jeremy = turtle.Turtle()
Jeremy.color("white")
Jeremy.shape("triangle")
Jeremy.penup()




#Create goal
goal = turtle.Turtle()
goal.color("pink")
goal.shape("circle")
goal.penup()
goal.speed(0)
goal.setposition(random.randint(-399,399), random.randint(-399, 399))




#Set speed variable
speed = 1

#Define functions

def turnleft():
    Jeremy.left(30)
    
def turnright():
    Jeremy.right(30)

def startforward():
    global speed
    #if speed == 1:
    print("")
    #else:
    speed +=1

def startback():
    global speed
    #if speed == -1:
    #print("")
    #else:
    speed -=1

def isCollision(t1, t2):
    d = math.sqrt(math.pow(t1.xcor()-t2.xcor(),2) + math.pow(t1.ycor()-t2.ycor(),2))
    if d < 15:
        return True
    else:
        return False

        
#Set keyboard bindings
turtle.listen()
turtle.onkey(turnleft, "Left") # Turn left for left arrowKey
turtle.onkey(turnright, "Right") #Turn right for right arrowKey
turtle.onkey(startback, "Down") #Forwards
turtle.onkey(startforward, "Up") #Backwards



while True:
    Jeremy.forward(speed)

    #Boundary Checking for Jeremy/Player
    if Jeremy.xcor() > 400 or Jeremy.xcor() < -400 :
        Jeremy.right(180)
        Jeremy.forward(100)
    if Jeremy.ycor() > 400 or Jeremy.ycor() < -400 :
        Jeremy.right(180)
        Jeremy.forward(100)
    #Boudary Checking for Goal
    if goal.xcor() > 200 or goal.xcor() < -200 :
        goal.right(180)
    if goal.ycor() > 200 or goal.ycor() < -200 :
        goal.right(180)
        
    

    
    #Collision checking
    
    if isCollision(Jeremy, goal):
        winsound.Beep(1010,100)
        winsound.Beep(1030,75)
        goal.setposition(random.randint(-200,200), random.randint(-200, 200))

    #moe goal
    
    goal.forward(1)



delay = input("Press enter to finish")



        
