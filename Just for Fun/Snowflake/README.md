# Snowflake.py

###### Developed by Sunghyun Cho on July 6th, 2018.

### Feature

Draws SnowFlake with Python Turtle Graphics

![Snowflake.gif](https://github.com/anaclumos/Programming/blob/master/Just%20for%20Fun/Snowflake/Snowflake.gif)

### Code

```python
from turtle import *
import time

def broccolify(currentPos, forwardLength, tiltDeg, terminatingLength):
	
	if forwardLength >= terminatingLength:

		turtle = Turtle()
		turtle.speed('fastest')

		turtle.hideturtle()
		turtle.penup()
		turtle.setpos(currentPos)
		turtle.pendown()
		turtle.setheading(tiltDeg)
		turtle.forward(forwardLength)

		pos = turtle.pos()
		tilt= tiltDeg

		broccolify(pos, forwardLength/(3), tilt + 120, terminatingLength)
		broccolify(pos, forwardLength/(3), tilt + 60 , terminatingLength)
		broccolify(pos, forwardLength/(3), tilt      , terminatingLength)
		broccolify(pos, forwardLength/(3), tilt - 60 , terminatingLength)
		broccolify(pos, forwardLength/(3), tilt - 120, terminatingLength)

screen = Screen()
screen.tracer(1,1)

recurseNum = int(input("recurseNum? : "))

terminateAt = 100/((3)**(recurseNum))

start_time = time.time()

broccolify((0, 0), 100, 60, terminateAt)
broccolify((0, 0), 100, 120, terminateAt)
broccolify((0, 0), 100, 180, terminateAt)
broccolify((0, 0), 100, 240, terminateAt)
broccolify((0, 0), 100, 300, terminateAt)
broccolify((0, 0), 100, 0, terminateAt)

string = ("     Time : " + str(int((time.time() - start_time)*1000)/1000) + "seconds\n     Stage: "+str(recurseNum))

turtle = Turtle()
turtle.hideturtle()
turtle.penup()
turtle.goto(-180, -300)
turtle.write(string, move=False, align="left", font=("SF Mono", 20, "normal"))

input("Press Return to Terminate Program. ")
```
