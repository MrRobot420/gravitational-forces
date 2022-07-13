import math
import random
import pygame
import pymunk
import pymunk.pygame_util

from sun import Sun
from planet import Planet
from font import Font
from utils import calculate_distance

pygame.init()

WIDTH, HEIGHT = 1600, 950
window = pygame.display.set_mode((WIDTH, HEIGHT))


class SolarSystem:
    def __init__(self):
        self.running = True
        self.clock = pygame.time.Clock()
        self.fps = 60
        self.dt = 1 / self.fps
        self.space = pymunk.Space()
        self.space.gravity = (0.0, 0.0)
        self.planets = []
        self.moons = []

        self.sun = Sun(self.space, 24, 500, (WIDTH / 2, HEIGHT / 2))

        self.all_sprites = pygame.sprite.Group()

    def run(self, window):
        draw_options = pymunk.pygame_util.DrawOptions(window)

        while self.running:
            self.update_text()

            self.handle_events()
            self.handle_gravity()
            self.draw(window, draw_options)

            self.space.step(self.dt)
            self.clock.tick(self.fps)

    def update_text(self):
        pl_text_pos = (WIDTH - 250, 0 + 20)
        pl_text = f'Planets: {len(self.planets)}'
        self.pl_font = Font(window, 24, pl_text_pos, pl_text)
        moon_text_pos = (WIDTH - 100, 0 + 20)
        moon_text = f'Moons: {len(self.moons)}'
        self.moon_font = Font(window, 24, moon_text_pos, moon_text)

    def draw(self, window, draw_options):
        window.fill("black")
        self.pl_font.show()
        self.moon_font.show()
        self.space.debug_draw(draw_options)
        pygame.display.update()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                self.execute_mouse_event()

    def execute_mouse_event(self):
        leftclick, middleclick, rightclick = pygame.mouse.get_pressed()
        pos = pygame.mouse.get_pos()

        if leftclick:
            radius = random.randint(1, 2)
            mass = random.randint(radius * 1, radius * 10)
            self.moons.append(Planet(self.space, self.sun, pos, radius, mass))
        if rightclick:
            radius = random.randint(8, 12)
            mass = random.randint(radius * 80, radius * 100)
            self.planets.append(
                Planet(self.space, self.sun, pos, radius, mass))
        if middleclick:
            self.space.remove(self.sun.body, self.sun.shape)
            self.sun = Sun(self.space, 24, 500, pygame.mouse.get_pos())

    def handle_gravity(self):
        self.handle_objects(self.planets)
        self.handle_objects(self.moons)

    def handle_objects(self, objects):
        border = 1000
        previous_object = None
        for obj in objects:
            for moon in self.moons:
                self.calc_gravitational_impact_planet(obj, moon)
                moon.move()
            if previous_object is not None:
                self.calc_gravitational_impact_planet(previous_object, obj)
                obj.move()

            self.calc_gravitational_impact_sun(self.sun, obj)
            if obj.body.position.x < 0 - border or obj.body.position.x > WIDTH + border:
                objects.remove(obj)
                self.space.remove(obj.body, obj.shape)
            elif obj.body.position.y < 0 - border or obj.body.position.y > HEIGHT + border:
                objects.remove(obj)
                self.space.remove(obj.body, obj.shape)
            else:
                previous_object = obj
                obj.move()

    def calc_gravitational_impact_sun(self, first, second):
        distance = calculate_distance(first, second)
        force = first.mass * second.mass / distance ** 2
        angle = first.body.velocity.get_angle_between(second.body.velocity)
        reverse_x = 1
        reverse_y = 1
        for object in first, second:
            acceleration = force / object.mass

            acc_x = acceleration * math.cos(math.radians(angle))
            acc_y = acceleration * math.cos(math.radians(angle))
            if object.body.position.x < self.sun.x:
                reverse_x = 1
            else:
                reverse_x = -1

            if object.body.position.y < self.sun.y:
                reverse_y = 1
            else:
                reverse_y = -1

            object.body.velocity = (
                object.body.velocity[0] + (reverse_x * acc_x),
                object.body.velocity[1] + (reverse_y * acc_y),
            )

    def calc_gravitational_impact_planet(self, first, second):
        distance = calculate_distance(first, second)
        if distance > 0:
            force = first.mass * second.mass / distance ** 2
        else:
            return
        angle = first.body.velocity.get_angle_between(
            second.body.velocity)
        reverse_x = 1
        reverse_y = 1

        acceleration = force / second.mass
        acc_x = acceleration / 20 * math.cos(math.radians(angle))
        acc_y = acceleration / 20 * math.cos(math.radians(angle))

        if second.body.position.x < first.body.position.x:
            reverse_x = 1
        else:
            reverse_x = -1

        if second.body.position.y < first.body.position.y:
            reverse_y = 1
        else:
            reverse_y = -1

        second.body.velocity = (
            second.body.velocity[0] + (reverse_x * acc_x),
            second.body.velocity[1] + (reverse_y * acc_y),
        )


if __name__ == "__main__":
    solar_system = SolarSystem()
    solar_system.run(window)
