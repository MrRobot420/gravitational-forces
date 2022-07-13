import random
import math


def get_random_color():
    red = random.randint(50, 255)
    green = random.randint(50, 255)
    blue = random.randint(50, 255)
    return (red, green, blue, 100)


def get_random_velocity():
    Vx = random.randint(-50, 50)
    Vy = random.randint(-50, 50)
    return (Vx, Vy)


def calculate_distance(sun, planet):
    return math.sqrt((sun.body.position[0] - planet.body.position[0])**2 + (sun.body.position[1] - planet.body.position[1])**2)
