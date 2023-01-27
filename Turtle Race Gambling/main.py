from turtle import Turtle, Screen
import random


screen = Screen()
screen.title("Turtle Race")
screen.setup(width=500, height=400)

colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [-100, -60, -20, 20, 60, 100]


def guess():
    user_guess = screen.textinput(title="Make your bet", prompt="Which turtle will win the race?\nEnter one of the "
                                                                "following colors:\nred, orange, yellow, green, "
                                                                "blue or purple: ")
    if user_guess in colors:
        return user_guess
    else:
        screen.clear()
        guess()


def race():
    is_racing = False
    all_turtles = []
    user_guess = guess()

    for turtle_index in range(6):
        new_turtle = Turtle(shape="turtle")
        new_turtle.color(colors[turtle_index])
        new_turtle.penup()
        new_turtle.goto(x=-230, y=y_positions[turtle_index])
        all_turtles.append(new_turtle)

    if user_guess:
        is_racing = True

    while is_racing:
        for turtle in all_turtles:
            if turtle.xcor() > 230:
                is_racing = False
                winning_color = turtle.pencolor()
                if winning_color == user_guess:
                    again = screen.textinput(title="Result", prompt=f"You've won! The {winning_color} turtle is the "
                                                                    f"winner!\nWould you like to try again? Type 'y' "
                                                                    f"or 'n'")
                    if again == "y":
                        screen.clear()
                        race()
                    else:
                        screen.bye()
                else:
                    again = screen.textinput(title="Result", prompt=f"You've lost! The {winning_color} turtle is the "
                                                                    f"winner!\nWould you like to try again? Type 'y' "
                                                                    f"or 'n'")
                    if again == "y":
                        screen.clear()
                        race()
                    else:
                        screen.bye()
            turtle.forward(random.randint(0, 10))


race()
