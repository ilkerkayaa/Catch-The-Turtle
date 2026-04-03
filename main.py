import turtle
import random

screen = turtle.Screen()
screen.bgcolor("light blue")
screen.title("Catch The Turtle")
FONT = ("Courier", 20, "normal")

grid_size = 10

# turtle list
turtle_list = []

score = 0

# countdown turtle
countdown_turtle = turtle.Turtle()

# score turtle
score_turtle = turtle.Turtle()

def setup_score_turtle():
    score_turtle.hideturtle()
    score_turtle.color("dark blue")
    score_turtle.penup()

    top_height = screen.window_height() / 2
    y = top_height * 0.8
    score_turtle.setposition(0, y)
    score_turtle.write(arg= "Score: 0", move = False, align= "center", font= FONT)

def make_turtle(x, y):

    t = turtle.Turtle()

    def handle_click(x, y):
        global score
        score += 1
        score_turtle.clear()
        score_turtle.write(arg= f"Score: {score}", move = False, align= "center", font= FONT)

    t.onclick(handle_click)
    t.penup()
    t.shape("turtle")
    t.color("green")
    t.shapesize(2)
    t.goto(x * grid_size, y * grid_size)
    turtle_list.append(t)

x_cordinates = [-20, -10, 0, 10, 20]
y_cordinates = [-20, -10, 0, 10]

def setup_turtles():
    for x in x_cordinates:
        for y in y_cordinates:
            make_turtle(x, y)

def hide_turtles():
    for t in turtle_list:
        t.hideturtle()

# recursive function
def show_turtles():
    hide_turtles()
    random.choice(turtle_list).showturtle()
    screen.ontimer(show_turtles, 500)

def countdown(time):
    countdown_turtle.hideturtle()
    countdown_turtle.penup()
    top_height = screen.window_height() / 2
    y = top_height * 0.8
    countdown_turtle.setposition(0, y -30)

    if time > 0:
        countdown_turtle.clear()
        countdown_turtle.write(arg=f"Time: {time}", move=False, align="center", font=FONT)

turtle.tracer(0)

setup_score_turtle()
setup_turtles()
hide_turtles()
show_turtles()
countdown(20)
turtle.tracer(1)

turtle.mainloop()