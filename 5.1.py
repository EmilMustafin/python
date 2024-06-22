import turtle
import math

square_side = int(input("сторона квадрата: "))
n = int(input("количество вложений: "))
turtle.hideturtle()
turtle.pencolor('white')
turtle.left(90)
turtle.forward(square_side/2)
turtle.left(90)
turtle.forward(square_side/2)
turtle.left(180)
turtle.pencolor('black')

turtle.speed(speed=9)
turtle.shape("turtle")
for i in range(4):
    turtle.forward(square_side)
    turtle.right(90)
turtle.right(90)
turtle.forward(square_side - ((square_side * math.sqrt(3))/2))
turtle.left(90)
for _ in range(3):
    turtle.forward(square_side)
    turtle.right(120)
turtle.forward(square_side / 2)
turtle.right(180)
radius = ((square_side * square_side * math.sqrt(3))/ 4) / ((square_side * 3)/2)
turtle.circle(radius)

if n > 1 and n < 5:
    for _ in range(n - 1):
        turtle.pencolor('white')
        turtle.left(90)
        turtle.forward(radius)
        turtle.right(90+45)
        turtle.forward(radius)
        turtle.right(90+45)
        turtle.pencolor('black')
        square_side = math.sqrt(2) * radius
        for i in range(4):
            turtle.forward(square_side)
            turtle.right(90)
        turtle.right(90)
        turtle.forward(square_side - ((square_side * math.sqrt(3))/2))
        turtle.left(90)
        for _ in range(3):
            turtle.forward(square_side)
            turtle.right(120)
        turtle.forward(square_side / 2)
        turtle.right(180)
        radius = ((square_side * square_side * math.sqrt(3))/ 4) / ((square_side * 3)/2)
        turtle.circle(radius)


turtle.exitonclick()

