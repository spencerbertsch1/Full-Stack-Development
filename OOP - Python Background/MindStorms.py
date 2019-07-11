# Drawing shapes with objects

#Imports
import turtle

def draw_square(square_turtle):
    # Draw a square
    for i in range(4):
        square_turtle.forward(170)  # moves turt forward by 170 pixels
        square_turtle.right(90)  # turns our turtle 90 degrees

def draw_circle(circle_turtle):
    circle_turtle.circle(100)

def draw_traingle(triangle_turtle):
    # Draw a square
    for i in range(3):
        triangle_turtle.forward(50)  # moves turt forward by 100 pixels
        triangle_turtle.left(120)  # turns our turtle 120 degrees

def draw_art():
    # create background screen for drawing
    window = turtle.Screen()
    window.bgcolor("black")

    # instantiate a turtle object which we can design and then pass to the 'draw square' function
    turt = turtle.Turtle()
    turt.shape("turtle")
    turt.color("yellow")
    turt.speed(2)
    draw_square(turt)

    # Instantiate another turtle object named 'angie'
    #angie = turtle.Turtle()
    #angie.shape("arrow")
    #angie.color("blue")
    #Draw a circle
    #draw_circle(angie)

    window.exitonclick()


def draw_square_circle():
    # create background screen for drawing
    window = turtle.Screen()
    window.bgcolor("black")

    # instantiate a turtle object which we can design and then pass to the 'draw square' function
    turt = turtle.Turtle()
    turt.shape("turtle")
    turt.color("yellow")
    turt.speed(8)

    for i in range(0,48):
        draw_square(turt)
        turt.right(7.5)

    window.exitonclick()


def draw_fractal():
    # create background screen for drawing
    window = turtle.Screen()
    window.bgcolor("black")

    # instantiate a turtle object which we can design and then pass to the 'draw square' function
    turt = turtle.Turtle()
    turt.shape("turtle")
    turt.color("yellow")
    turt.speed(8)

    for i in range(0,2):
        draw_traingle(turt)
        turt.forward(50)

    window.exitonclick()


draw_fractal()