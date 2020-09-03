import random
import pygame

from config_manager import *


class Snake:
    def __init__(self, player):
        self.player = player
        self._put_on_screen()

        if player == Player.PLAYER_1:
            self.color = Color.SNAKE_1.value
            self.frame_color = Color.SNAKE_1_FRAME.value
        else:
            self.color = Color.SNAKE_2.value
            self.frame_color = Color.SNAKE_2_FRAME.value

    def _put_on_screen(self):
        self.length = 1
        self.positions = [START_POSITION1] if self.player == Player.PLAYER_1 else [START_POSITION2]
        self.direction = random.choice([UP, DOWN, LEFT, RIGHT])

        self.can_change_direction = True
        self.future_direction = None

    def get_head_position(self):
        return self.positions[0]

    def turn(self, new_direction):
        new_direction_is_reverse_of_current_direction = (new_direction[0] * -1 == self.direction[0]) and \
                                                        (new_direction[1] * -1 == self.direction[1])
        if new_direction_is_reverse_of_current_direction:
            return  # snake cannot reverse it's direction

        elif self.can_change_direction:
            self.direction = new_direction  # set new direction
            self.can_change_direction = False  # snake cannot change it's direction multiple times in 1 move
        else:  # snake already changed it's direction at this move:
            self.future_direction = new_direction  # remember future direction for following move

    def move(self, other_snake_positions):
        head_x, head_y = self.get_head_position()
        step_x, step_y = self.direction
        new_head = (((head_x + (step_x*GRIDSIZE)) % SCREEN_WIDTH), ((head_y + (step_y*GRIDSIZE)) % SCREEN_HEIGHT))

        self.positions.insert(0, new_head)
        if new_head in self.positions[3:]:
            return True  # snake eat itself - Game over

        if other_snake_positions is not None and new_head in other_snake_positions:
            return True  # snake eat another snake - Game over

        if len(self.positions) > self.length:  # did not found food:
            self.positions.pop()  # tail progress

        if self.future_direction:  # if snake has planes to change it's direcion - apply them
            self.direction = self.future_direction
            self.future_direction = None
        else:
            self.can_change_direction = True

    def shorten(self, how_much_to_cut):
        how_much_to_cut = min(how_much_to_cut, self.length-1)
        self.length -= how_much_to_cut
        if self.length > 1:
            self.positions = self.positions[:-how_much_to_cut]


    def reset(self):
        self._put_on_screen()

    def _get_choose_snake_color_acording_to_power_ups(self, game_status):
        if Status.SPEED_POWERUP_DURATION in game_status.keys() and Status.SCORE_POWER_UP_DURATION in game_status.keys():
            return Color.DOUBLESPEED_AND_DOUBLESCORE_SNAKE.value
        elif Status.SPEED_POWERUP_DURATION in game_status.keys():
            return Color.DoubleSpeed_SNAKE.value
        elif Status.SCORE_POWER_UP_DURATION in game_status.keys():
            return Color.DoubleScore_SNAKE.value
        else:
            return self.color

    def draw(self, surface, game_status):
        snake_color = self._get_choose_snake_color_acording_to_power_ups(game_status)

        # draw head
        head_x, head_y = self.positions[0]
        r = pygame.Rect((int(head_x), int(head_y)), (int(GRIDSIZE*6/5), int(GRIDSIZE*6/5)))
        pygame.draw.ellipse(surface, snake_color, r)
        pygame.draw.ellipse(surface, self.frame_color, r, 1)

        # draw tail
        tail_x, tail_y = self.positions[-1]
        if len(self.positions) > 1:
            r = pygame.Rect((int(tail_x), int(tail_y)), (int(GRIDSIZE*5/6), int(GRIDSIZE*5/6)))
            pygame.draw.ellipse(surface, snake_color, r)
            pygame.draw.ellipse(surface, self.frame_color, r, 1)

        # draw body
        for body_x, body_y in self.positions[1:-1]:
            r = pygame.Rect((int(body_x), int(body_y)), (GRIDSIZE, GRIDSIZE))
            pygame.draw.rect(surface, snake_color, r)
            pygame.draw.rect(surface, self.frame_color, r, 1)