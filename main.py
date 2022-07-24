import turtle

screen = turtle.Screen()
screen.title("U.S. States Game")

# adding gif image file to screen and using it as shape
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

screen.exitonclick()
