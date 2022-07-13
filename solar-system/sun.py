import scipy as sp
import pymunk


class Sun:
    def __init__(self, space, radius, mass, pos):
        self.space = space
        self.radius = radius
        self.mass = mass
        self.body = pymunk.Body(body_type=pymunk.Body.STATIC)
        self.body.position = pos
        self.x = pos[0]
        self.y = pos[1]

        self.shape = pymunk.Circle(self.body, radius)
        self.shape.mass = mass
        self.shape.elasticity = 0
        self.shape.friction = 1
        self.shape.color = (255, 255, 50, 100)
        self.space.add(self.body, self.shape)

    def move(self):
        self.body.position += self.body.velocity
