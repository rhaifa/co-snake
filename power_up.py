import random
from abc import abstractmethod


from config_manager import Color, Status, GRIDSIZE
from eatable_object import EatableObject
from game import choose_power_up


class PowerUp(EatableObject):
    text = None
    text_color = None

    def __init__(self):
        super().__init__()
        self.activation_duration = random.randint(3, 7)  # amount of seconds the effect will hold

    @abstractmethod
    def active(self, game_status, snakes):
        """active the effect of the power up."""
        raise NotImplementedError

    def write_text(self, screen, game_font):
        if self.text:
            text = game_font.render(self.text, 1, self.text_color)
            screen.blit(text, (self.position[0] + GRIDSIZE, self.position[1] + GRIDSIZE))


class DoubleSpeed(PowerUp):
    img = None
    text = "X2 SPEED"
    text_color = Color.DoubleSpeed_TEXT.value

    def active(self, game_status, snakes):
        game_status[Status.SPEED] *= 2
        game_status[Status.SPEED_POWERUP_DURATION] = self.activation_duration


class DoubleScore(PowerUp):
    img = None
    text = "X2 SCORE"
    text_color = Color.DoubleScore_TEXT.value

    def active(self, game_status, snakes):
        game_status[Status.SCORE_FACTOR] *= 2
        game_status[Status.SCORE_POWER_UP_DURATION] = self.activation_duration * 2


class ShortenSnake(PowerUp):
    img = None

    def active(self, game_status, snakes):
        how_much_to_cut = random.randint(2, 4)
        for snake in snakes:
            snake.shorten(how_much_to_cut)


class RandomPowerup(PowerUp):
    img = None

    def active(self, game_status, snakes):
        p = random.choice([DoubleSpeed(), DoubleScore(), ShortenSnake()])
        p.active(game_status, snakes)

