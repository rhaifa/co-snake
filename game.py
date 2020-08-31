from food import *
from power_up import *
from snake import *
import os


def draw_grid(surface):
    for y in range(0, int(GRID_HEIGHT)):
        for x in range(0, int(GRID_WIDTH)):
            r = pygame.Rect((x * GRIDSIZE, y * GRIDSIZE), (GRIDSIZE, GRIDSIZE))
            pygame.draw.rect(surface, Color.GRID_1.value, r)


def get_new_game_status():
    return {Status.SCORE: BASE_GAME_SCORE,
            Status.SPEED: BASE_GAME_SPEED,
            Status.SCORE_FACTOR: BASE_GAME_SCORE_FACTOR}


def _draw_everthing_on_screen(power_up, snakes, game_status, food, surface, screen, game_font):
    for snake in snakes:
        snake.draw(surface, game_status)
    food.draw(surface)
    if power_up:
        power_up.draw(surface)
    screen.blit(surface, (0, 0))

    if power_up:
        power_up.write_text(screen, game_font)

    # draw players scores:
    text_player_1 = game_font.render(f"Score {game_status[Status.SCORE]}", 1, Color.FONT_1.value)
    screen.blit(text_player_1, (SCREEN_WIDTH - 100, 10))
    if len(snakes) == 1:
        text_player_2 = game_font.render(f"Player2: press space to join", 1, Color.FONT_2.value)
    else:
        text_player_2 = game_font.render(f"Keys: w,a,s,d", 1, Color.FONT_2.value)
    screen.blit(text_player_2, (5, 10))
    pygame.display.update()


def handle_power_up(power_up, snake, game_status):
    if power_up is None and 0 <= pygame.time.get_ticks() % 300 <= 10:  # after some time there is no power up on screen
        power_up = random.choice([DoubleSpeed(), DoubleScore()])  # create it

    if power_up is not None:
        if snake.get_head_position() == power_up.get_position():  # if snake eat power up
            power_up.active(game_status)  # active it's effect
            power_up = None  # remove power up

    # TODO handle this better
    # if speed power up duration has finished, remove it's effect
    if Status.SPEED_POWERUP_DURATION in game_status.keys():
        game_status[Status.SPEED_POWERUP_DURATION] -= 0.1
        if game_status[Status.SPEED_POWERUP_DURATION] < 0:
            del game_status[Status.SPEED_POWERUP_DURATION]
            game_status[Status.SPEED] = BASE_GAME_SPEED

    # if Score power up duration has finished, remove it's effect
    if Status.SCORE_POWER_UP_DURATION in game_status.keys():
        game_status[Status.SCORE_POWER_UP_DURATION] -= 0.1
        if game_status[Status.SCORE_POWER_UP_DURATION] < 0:
            del game_status[Status.SCORE_POWER_UP_DURATION]
            game_status[Status.SCORE_FACTOR] = BASE_GAME_SCORE_FACTOR

    return power_up


def handle_keys(snakes):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                snakes[0].turn(UP)
            elif event.key == pygame.K_DOWN:
                snakes[0].turn(DOWN)
            elif event.key == pygame.K_LEFT:
                snakes[0].turn(LEFT)
            elif event.key == pygame.K_RIGHT:
                snakes[0].turn(RIGHT)
            elif event.key == pygame.K_SPACE and len(snakes) == 1:
                snakes.append(Snake(Player.PLAYER_2))
            if len(snakes) >= 2:
                if event.key == pygame.K_w:
                    snakes[1].turn(UP)
                if event.key == pygame.K_s:
                    snakes[1].turn(DOWN)
                if event.key == pygame.K_a:
                    snakes[1].turn(LEFT)
                if event.key == pygame.K_d:
                    snakes[1].turn(RIGHT)


def reset_snakes(snakes):
    pygame.time.wait(GAME_OVER_DELAY)
    for snake in snakes:
        snake.reset()


def get_other_snake_positions(snakes, number_of_players, i):
    if number_of_players == 1:
        return None
    if i == 0:
        return snakes[1].positions
    return snakes[0].positions


def update_hall_of_fame(new_score):
    """:return boolean - True if new scored enter 'hall_of_fame', else False """
    # file does not exist -> create it
    if not os.path.isfile(HALL_OF_FAME_FILE_NAME):
        with open(HALL_OF_FAME_FILE_NAME, "w") as file1:
            file1.write(str(new_score))
        return True

    # file exist:
    with open(HALL_OF_FAME_FILE_NAME, "r+") as file1:
        scores_string = file1.read()
    current_scores = [int(score) for score in scores_string.split(",")]
    current_min = min(current_scores)
    if len(current_scores) < HALL_OF_FAME_SCORES_MAX_AMOUNT or new_score > current_min:
        if len(current_scores) < HALL_OF_FAME_SCORES_MAX_AMOUNT:  # there is a slot left -> enter the new score
            current_scores.append(new_score)
        elif new_score > current_min:  # new score is higher then current score-> replace old score with new score
            current_scores[current_scores.index(current_min)] = new_score
            print("you are a champion")

        scores_string = ",".join([str(score) for score in sorted(current_scores, reverse=True)])
        with open(HALL_OF_FAME_FILE_NAME, "w") as file1:
            file1.write(str(scores_string))
        return True
    # didn't enter hall of fame
    return False


def print_hall_of_fame(enter_hall_of_fame, new_score, screen, hall_of_fame_font, medal_gold, medal_silver, medal_bronze):
    screen.fill((40, 40, 40))
    text = hall_of_fame_font.render("Hall Of Fame", 1, Color.FONT_1.value)
    x_pos, y_pos = int(SCREEN_WIDTH / 3), 50
    screen.blit(text, (x_pos, y_pos))

    with open(HALL_OF_FAME_FILE_NAME, "r+") as file:
        scores = file.read().split(",")

    for place, score in enumerate(scores):
        if enter_hall_of_fame and str(new_score) == score:
            text = hall_of_fame_font.render(f"{score} (you)", 1, Color.FONT_2.value)
            enter_hall_of_fame = False
        else:
            text = hall_of_fame_font.render(score, 1, Color.FONT_1.value)
        y_pos = y_pos + 50
        screen.blit(text, (x_pos, y_pos))
        medal = None
        if place == 0:
            medal = medal_gold
        elif place == 1:
            medal = medal_silver
        elif place == 2:
            medal = medal_bronze
        if medal is not None:
            screen.blit(medal, (x_pos - GRIDSIZE * 5, y_pos))
    pygame.display.update()
    pygame.time.delay(GAME_OVER_DELAY * 2)


def print_game_over(screen, game_over_img):
    screen.blit(game_over_img, (int(SCREEN_WIDTH / 2 - GRIDSIZE*3), int(SCREEN_HEIGHT / 2 - GRIDSIZE*3)))
    pygame.display.update()
    pygame.time.delay(GAME_OVER_DELAY)


def main():
    # Initialize the pygame
    pygame.init()

    # create the screen
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), 0, 32)
    surface = pygame.Surface(screen.get_size())  # .convert()
    draw_grid(surface)

    # Title and Icon
    pygame.display.set_caption("Co-Snake")
    icon = pygame.image.load("icons/snake_icon.png")
    pygame.display.set_icon(icon)

    # load all the game pictures into 'image_dict'
    icons_directory = "icons"
    image_filenames = os.listdir(icons_directory)  # returns list
    image_dict = dict()
    for image_file in image_filenames:
        without_suffix = image_file.split(".")[0]
        image_dict[without_suffix] = pygame.image.load(os.path.join(icons_directory, image_file))

    large_greed = int(GRIDSIZE * 1.3)
    Apple.img = pygame.transform.scale(image_dict['apple'], (large_greed, large_greed))
    Banana.img = pygame.transform.scale(image_dict['banana'], (large_greed, large_greed))
    DoubleScore.img = pygame.transform.scale(image_dict['double_score'], (large_greed, large_greed))
    DoubleSpeed.img = pygame.transform.scale(image_dict['double_speed'], (large_greed, large_greed))
    game_over_img = pygame.transform.scale(image_dict['game_over'], (GRIDSIZE*6, GRIDSIZE*6))
    medal_size = (GRIDSIZE*3, GRIDSIZE*3)
    medal_gold = pygame.transform.scale(image_dict['medal_gold'], medal_size)
    medal_silver = pygame.transform.scale(image_dict['medal_silver'], medal_size)
    medal_bronze = pygame.transform.scale(image_dict['medal_bronze'], medal_size)

    clock = pygame.time.Clock()
    game_font = pygame.font.SysFont("monospace", 16)
    hall_of_fame_font = pygame.font.SysFont("monospace", 28)

    snakes = [Snake(Player.PLAYER_1)]
    food = Apple()
    power_up = DoubleScore()
    game_status = get_new_game_status()
    while True:
        clock.tick(game_status[Status.SPEED])
        handle_keys(snakes)
        number_of_players = len(snakes)
        draw_grid(surface)

        for i, snake in enumerate(snakes):
            game_over = snake.move(other_snake_positions=get_other_snake_positions(snakes, number_of_players, i))
            if game_over:
                print_game_over(screen, game_over_img)
                enter_hall_of_fame = update_hall_of_fame(game_status[Status.SCORE])
                print_hall_of_fame(enter_hall_of_fame, game_status[Status.SCORE], screen, hall_of_fame_font, medal_gold,
                                   medal_silver, medal_bronze)
                reset_snakes(snakes)
                game_status = get_new_game_status()

            if snake.get_head_position() == food.position:
                snake.length += 1
                game_status[Status.SCORE] = game_status[Status.SCORE] + (food.get_nutrition_value() * game_status[Status.SCORE_FACTOR])
                food = random.choice([Apple(), Banana()])
            power_up = handle_power_up(power_up, snake, game_status)
        _draw_everthing_on_screen(power_up, snakes, game_status, food, surface, screen, game_font)







if __name__ == '__main__':
    main()