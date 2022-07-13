import pygame


class Font:
    def __init__(self, screen, font_size, dimensions, text):
        self.screen = screen
        self.font = pygame.font.SysFont("Arial", font_size)
        primary_color = (255, 255, 255)
        self.text = self.font.render(
            text, True, primary_color)

        self.x, self.y = dimensions
        self.textRect = self.text.get_rect()
        self.textRect.center = (self.x, self.y)

    def show(self):
        self.screen.blit(self.text, self.textRect)
