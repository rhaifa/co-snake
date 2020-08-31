from enum import Enum

# GAME SETTINGS
BASE_GAME_SPEED = 8
BASE_GAME_SCORE = 0
BASE_GAME_SCORE_FACTOR = 1
GAME_OVER_DELAY = 3000

# HALL OF FAME
HALL_OF_FAME_SCORES_MAX_AMOUNT = 3
HALL_OF_FAME_FILE_NAME = 'hall_of_fame.txt'

# SCREEN
SCREEN_WIDTH = 480
SCREEN_HEIGHT = 480
SCREEN_CENTER = ((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2))
START_POSITION1 = ((SCREEN_WIDTH * 2 / 3), (SCREEN_HEIGHT * 2 / 3))
START_POSITION2 = ((SCREEN_WIDTH / 3), (SCREEN_HEIGHT / 3))
GRIDSIZE = 20
GRID_WIDTH = SCREEN_HEIGHT/GRIDSIZE
GRID_HEIGHT = SCREEN_WIDTH/GRIDSIZE

# DIRECTIONS
UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)


class Status(Enum):  # Status of the game
    SCORE = 1
    SPEED = 2
    SCORE_FACTOR = 3  # every time you earn x scores, they are multiply by this factor
    SPEED_POWERUP_DURATION = 4
    SCORE_POWER_UP_DURATION = 5


class Shapes(Enum):
    RECT = 1
    Ellipsis = 2

class Player(Enum):
    PLAYER_1 = 1
    PLAYER_2 = 2

class Color(Enum):
    GRID_1 = (60, 60, 60)

    FONT_1 = (93, 216, 0)
    SNAKE_1 = (17, 24, 47)
    SNAKE_1_FRAME = (93, 216, 0)

    FONT_2 = (240, 93, 10)
    SNAKE_2 = (17, 24, 47)
    SNAKE_2_FRAME = (216, 93, 0)

    # POWER UPS:
    DoubleSpeed_TEXT = (255, 255, 255)
    DoubleSpeed_SNAKE = (240, 240, 0)

    DoubleScore_TEXT = (255, 255, 255)
    DoubleScore_SNAKE = (0, 200, 250)

    DOUBLESPEED_AND_DOUBLESCORE_SNAKE = (50, 200, 50)
