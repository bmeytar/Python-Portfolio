import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

my_screen = Screen()
my_screen.setup(width=600, height=600)
my_screen.title("Turtle Crossing")
my_screen.tracer(0)

player = Player()
scoreboard = Scoreboard()
car_manager = CarManager()

my_screen.listen()
my_screen.onkey(player.up, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    my_screen.update()

    if player.ycor() > 280:
        scoreboard.next_level()
        player.reset_position()
        car_manager.next_level()
    else:
        car_manager.create_car()
        car_manager.move_cars()

    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            scoreboard.game_over()
            game_is_on = False

my_screen.exitonclick()
