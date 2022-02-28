import turtle
import random
  
myTurtle = turtle.Turtle()
myWin = turtle.Screen()
  
def drawCircle(myTurtle,len):
    myTurtle.pensize(2)
    myTurtle.speed(20)
    rad = int(random.randint(45,135))
    i = 1

    def drawReal(i):
        myTurtle.backward(len)
        myTurtle.circle(len)
        myTurtle.right(rad)    

    while i < 40:
            print(i)
            i += 1  
            drawReal(i)


def drawSpiral(myTurtle,len):
    myTurtle.pensize(2)
    myTurtle.speed(40)  
    rad = int(random.randint(45,135))
    i = 1

    def drawReal(len):
        myTurtle.backward(len)
        myTurtle.right(rad) 
        len = len + 20


    while i < 200:
            print(i)
            i += 1  
            drawReal(i)

def drawWeierdSpiral(myTurtle,len):
    myTurtle.pensize(2)
    myTurtle.speed(40)  
    rad = int(random.randint(45,135))
    i = 1

    def drawReal(len):
        myTurtle.backward(len)
        myTurtle.circle(len/-10)
        myTurtle.right(rad) 
        len = len + 20


    while i < 200:
            print(i)
            i += 1  
            drawReal(i)


def chooseMode():
    seq = (1,2,3)
    choice = random.choice(seq)  

    if choice==1:
        drawCircle(myTurtle, len)
        myWin.exitonclick()
    elif choice==2:
        drawSpiral(myTurtle, len)
        myWin.exitonclick()
    elif choice==3:
        drawWeierdSpiral(myTurtle, len)
        myWin.exitonclick()


len = random.randint(100,100)
deg =random.randint(1,2)


chooseMode()
