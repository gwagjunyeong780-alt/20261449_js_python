##a = int(input("첫번째 값"))
##b = int(input("두번째 값"))

##result1 = a+b
##result2 = a-b
##result3 = a*b
##result4 = a/b

##print(result1)
##print(result2)
##print(result3)
##print(result4)

##data = '안녕' + \
       ##'하세요?' + \
     ##  '파이썬'
##print(data)

##data = '안녕\n파이썬\n화요일 수업이지'
##print(data)

##import turtle

##t = turtle.Turtle()
##t.speed(3)
##t.pensize(10)
##t.pencolor("red")
## turtle.shape('turtle')

## for _ in range(5):
   ## t.forward(200)
   ## t.right(144)    

## t.done()

import turtle
import random

r, g, b = 0.0, 0.0, 0.0

def screenleftclick(x, y):
    turtle.pencolor(r, g, b)
    turtle.pendown()
    turtle.goto(x, y)

def screenrightclick(x, y):
    turtle.penup()
    turtle.goto(x, y)

def screenmidclick(x, y):
    global r, g, b

    turtle.shapesize(random.randrange(1, 10))

    r = random.random()
    g = random.random()
    b = random.random()

turtle.title('거북이로 그림 그리기')
turtle.shape('turtle')
turtle.pensize(10)

turtle.onscreenclick(screenleftclick, 1)
turtle.onscreenclick(screenmidclick, 2)
turtle.onscreenclick(screenrightclick, 3)

turtle.done()
