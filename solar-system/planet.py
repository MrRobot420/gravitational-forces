import random
import pymunk
from utils import get_random_color, get_random_velocity


class Planet:
    def __init__(self, space, sun, pos, radius, mass=1):
        self.space = space
        self.center_x = sun.x
        self.center_y = sun.y
        self.radius = radius
        self.mass = mass
        self.color = get_random_color()

        self.body = pymunk.Body()
        self.body.position = pos
        self.body.velocity = (0, 0)

        self.shape = pymunk.Circle(self.body, self.radius)
        self.shape.mass = self.mass
        self.shape.elasticity = 0
        self.shape.friction = 1
        self.shape.color = self.color
        self.space.add(self.body, self.shape)

    def move(self):
        self.body.position += self.body.velocity
