import turtle
poly=turtle.Turtle()
side=int(input("How many sides do you want your poly to be?"))
for i in range(side):
    poly.pendown()
    poly.begin_poly()
    poly.forward(100)
    poly.right(360/side)
turtle.exitonclick()  # Keeps pycharm window open





