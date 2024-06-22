import turtle
import math

def draw_square(side_length):
    for _ in range(4):
        turtle.forward(side_length)
        turtle.right(90)

def draw_triangle(side_length):
    for _ in range(3):
        turtle.forward(side_length)
        turtle.right(120)

def draw_figure(side_length):
    draw_square(side_length)
    turtle.right(90)
    turtle.forward(side_length - (side_length * math.sqrt(3)) / 2)
    turtle.left(90)
    draw_triangle(side_length)
    turtle.forward(side_length / 2)
    turtle.right(180)
    radius = ((side_length ** 2) * math.sqrt(3)) / (4 * side_length * 3 / 2)
    turtle.circle(radius)
    return radius

def move_to_next_figure(radius):
    turtle.pencolor('white')
    turtle.left(90)
    turtle.forward(radius)
    turtle.right(135)
    turtle.forward(radius)
    turtle.right(135)
    turtle.pencolor('black')

square_side = int(input("сторона квадрата: "))
n = int(input("количество вложений: "))


turtle.hideturtle()
turtle.pencolor('white')
turtle.left(90)
turtle.forward(square_side / 2)
turtle.left(90)
turtle.forward(square_side / 2)
turtle.left(180)
turtle.pencolor('black')


radius = draw_figure(square_side)


if 1 < n < 5:
    for _ in range(n - 1):
        move_to_next_figure(radius)
        square_side = math.sqrt(2) * radius
        radius = draw_figure(square_side)


turtle.exitonclick()
