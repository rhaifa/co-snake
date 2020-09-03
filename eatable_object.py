from config_manager import *
import random


# TODO: convert to abstract class?
class EatableObject:
    img = None

    def __init__(self):
        self.position = None
        self.randomize_position()

    def randomize_position(self):
        self.position = (random.randint(0, GRID_WIDTH - 1) * GRIDSIZE, random.randint(0, GRID_HEIGHT - 1) * GRIDSIZE)

    def get_position(self):
        return self.position

    # TODO improve
    def draw(self, surface):
        surface.blit(self.__class__.img, (self.position[0], self.position[1]))
