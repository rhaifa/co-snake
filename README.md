# Co-Snake
Multiplayer cooperative snake game

<img src=https://github.com/rhaifa/co-snake/blob/master/icons/game_preview.png>

<b>Quick setup</b><br />
step1: Download the game<br />
step2: Install 'pygame' package (one option is to run 'pip install -r /path/to/requirements.txt' in your terminal)<br />
step3: run game.py<br />
<br />
<b>How to play:</b><br />
The goal of the game is to get the highest score. You achive this by eating food and power-ups.<br />
Once you eat yourself (or another snake) the game is over.<br />
<br />

<b>Foods:</b><br />
<img src=https://github.com/rhaifa/co-snake/blob/master/icons/apple.png width=30>Apple - equal 1 point<br />
<img src=https://github.com/rhaifa/co-snake/blob/master/icons/banana.png width=30>Banana - equal 3 point<br />
<br />

<b>Power Ups:</b><br />
<img src=https://github.com/rhaifa/co-snake/blob/master/icons/double_speed.png width=30>
DoubleSpeed - X2 the speed of the game for a short time (This is really a powerdown)<br />
<img src=https://github.com/rhaifa/co-snake/blob/master/icons/double_score.png width=30>
DoubleScore - X2 the score value of food for a short time<br />
<img src=https://github.com/rhaifa/co-snake/blob/master/icons/shorten_snake.png width=30>
ShortenSnake - Shorten the snakes by 2-4 tiles<br />
<img src=https://github.com/rhaifa/co-snake/blob/master/icons/random_powerup.png width=30>
RandomPowerup - choose randomly between all other powerups<br /><br />

<b>Power Ups Combos</b><br/>
The snakes can have multiple powerups active at the same time<br />
Examples:<br />
<img src=https://github.com/rhaifa/co-snake/blob/master/icons/snake_normal.png> Normal snake:<br />
<img src=https://github.com/rhaifa/co-snake/blob/master/icons/snake_double_speed.png> Snake with 'Double Speed' power up: the speed of this snake is x2<br />
<img src=https://github.com/rhaifa/co-snake/blob/master/icons/snake_double_score.png> Snake with 'Double Score' power up: the score value of food is x2<br />
<img src=https://github.com/rhaifa/co-snake/blob/master/icons/snake_double_score_and_double_speed.png>Snake with 'Double Speed' and 'Double Score' power up: the speed of this snake is x2 and the score value of food is x2<br />
Snake with 3 'Double Speed' power ups and 2 'Double Score' power ups:
the speed of the snake is X8 and the score value of food is x4 <br/>


Important: Every time a power up of the same type is taken, the duration of the old powerup is prolonged:<br/>
Example: if a snake has 'Double Score' power up that will last one more second, and then he eats 'Double Score' powerup
(that for this example will last 8 seconds), then the old 'Double Score' power up will last also 8 seconds (instead of 1)<br/>





<b>Multiplayer</b><br />
Press 'space' to join new snake.
2nd player keys are: <img src=https://github.com/rhaifa/co-snake/blob/master/icons/keyboard_player_2.png width=30>
This is cooperative game - power ups are activated on all the snakes regardless the snake that eat them.


