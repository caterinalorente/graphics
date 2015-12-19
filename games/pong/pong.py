import pygame, sys, random
from pygame.locals import *

# Initialize the game engine
pygame.init()

# Set FPS
fps = 30
fps_clock = pygame.time.Clock()

# Constants
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 400
BALL_RADIUS = 20
BALL_VELOCITY_INCREMENT = 1.3
GUTTER_SCREEN_WIDTH = 1
PAD_WIDTH = 8
PAD_HEIGHT = 80
PAD_SPEED = 10
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2
LEFT = "left"
RIGHT = "right"

# Define the colours to be used in RGB
BLACK = (0,0,0)
GREY = (128, 128, 128)
RED = (255,0,0)
WHITE = (255,255,255)

# Set size of the canvas
canvas = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Pong")

# Set the font
font = pygame.font.Font("./assets/joystix_monospace.ttf", 25)


def spawn_ball(direction):
    """
    Spawns the ball according to a direction given
    :param direction: LEFT, RIGHT
    :return: nothing
    """

    global ball_pos, ball_vel # these are vectors stored as lists

    ball_pos = [SCREEN_WIDTH/2, SCREEN_HEIGHT/2]
    ball_vel_x = random.randrange(4,7)
    ball_vel_y = random.randrange(4,7)

    if direction == LEFT:
        ball_vel_x *= -1
        ball_vel_y *= -1
    elif direction == RIGHT:
        ball_vel_y *= -1

    ball_vel = [ball_vel_x,ball_vel_y]


def new_game():
    """
    Sets the paddles to their start position and spawns the ball
    randomly left or right.

    :return: nothing
    """

    global left_pad_pos, right_pad_pos, left_pad_vel, right_pad_vel
    global score_1, score_2

    left_pad_pos = SCREEN_HEIGHT/2 - HALF_PAD_HEIGHT
    left_pad_vel = 0

    right_pad_pos = SCREEN_HEIGHT/2 - HALF_PAD_HEIGHT
    right_pad_vel = 0

    score_1 = 0
    score_2 = 0

    spawn_ball(random.choice([LEFT, RIGHT]))


def key_down(key):
    """
    Updates the velocity of the paddles according to the keys pressed.

    :param key: arrow up = right paddle up
                arrow down = right paddle down
                w or W = left paddle up
                s or S = left paddle down
    :return: nothing
    """

    global left_pad_vel, right_pad_vel

    if key == K_UP:
        right_pad_vel = PAD_SPEED * -1
    elif key == K_DOWN:
        right_pad_vel = PAD_SPEED
    if key == K_w:
        left_pad_vel = PAD_SPEED * -1
    elif key == K_s:
        left_pad_vel = PAD_SPEED


def key_up(key):
    """
    Set paddle velocity to zero when no keys are pressed.

    :param key:
    :return: nothing
    """

    global left_pad_vel, right_pad_vel

    if key == K_UP:
        right_pad_vel = 0
    elif key == K_DOWN:
        right_pad_vel = 0
    if key == K_w:
        left_pad_vel = 0
    elif key == K_s:
        left_pad_vel = 0


def update_score(direction):
    """
    The ball is spawned in the direction of the player who scored.
    Therefore:
        If ball is spawned to the right, player 2 scored.
        If ball is spawned to the left, player 1 scored.

    :param direction:
    :return: nothing
    """
    global score_1, score_2

    if direction == "right":
        score_2 += 1
    else:
        score_1 += 1


def bounce_ball_or_spawn_ball(paddle_pos, direction):
    """
    Check if the ball is inside the paddle boundaries and bounce back.
    Otherwise, update the score and spawn a new ball.

    :param paddle_pos:
    :param direction:
    :return: nothing
    """

    global ball_vel

    if paddle_pos < ball_pos[1] < paddle_pos + PAD_HEIGHT:
        # Increase velocity
        ball_vel[0] *= BALL_VELOCITY_INCREMENT
        ball_vel[1] *= BALL_VELOCITY_INCREMENT
        # Change direction
        ball_vel[0] *= -1
    else:
        update_score(direction)
        spawn_ball(direction)

new_game()

# Main game loop
while True:
    global score_1, score_2, left_pad_pos, right_pad_pos, ball_pos, ball_vel

    for event in pygame.event.get():
        # If user clicked close
        if (event.type == QUIT) or (event.type == KEYUP and event.key == K_ESCAPE):
            pygame.quit()
            sys.exit()
        elif event.type == KEYDOWN:
            key_down(event.key)
        elif event.type == KEYUP:
            key_up(event.key)

    # Clear the canvas and set background
    canvas.fill(BLACK)

    # Draw gutters
    pygame.draw.line(canvas, GREY, [PAD_WIDTH,0],[PAD_WIDTH,SCREEN_HEIGHT])
    pygame.draw.line(canvas, GREY, [SCREEN_WIDTH-PAD_WIDTH,0],[SCREEN_WIDTH-PAD_WIDTH,SCREEN_HEIGHT])

    # Update ball
    if (ball_pos[1] <= BALL_RADIUS) or (ball_pos[1] >= SCREEN_HEIGHT - BALL_RADIUS):
        ball_vel[1] *= -1

    ball_pos_x = ball_pos[0] + int(ball_vel[0])
    ball_pos_y = ball_pos[1] + int(ball_vel[1])
    ball_pos = [ball_pos_x, ball_pos_y]

    # Draw ball
    pygame.draw.circle(canvas, WHITE, [ball_pos_x, ball_pos_y], BALL_RADIUS)

    # Update paddle's vertical position. Keep paddle on the screen
    if ((left_pad_pos > 0) and (left_pad_vel < 0)) or ((left_pad_pos + PAD_HEIGHT < SCREEN_HEIGHT) and (left_pad_vel > 0)):
        left_pad_pos += left_pad_vel
    if ((right_pad_pos > 0) and (right_pad_vel < 0)) or ((right_pad_pos + PAD_HEIGHT < SCREEN_HEIGHT) and (right_pad_vel > 0)):
        right_pad_pos += right_pad_vel

    # Draw paddles - Left and right
    pygame.draw.rect(canvas, WHITE, [0,left_pad_pos,PAD_WIDTH,PAD_HEIGHT])
    pygame.draw.rect(canvas, WHITE, [SCREEN_WIDTH-PAD_WIDTH,right_pad_pos,PAD_WIDTH,PAD_HEIGHT])

    # Determine whether paddle and ball collide
    if ball_pos[0] - BALL_RADIUS <= PAD_WIDTH:
        bounce_ball_or_spawn_ball(left_pad_pos, RIGHT)
    elif ball_pos[0] + BALL_RADIUS >= SCREEN_WIDTH - PAD_WIDTH:
        bounce_ball_or_spawn_ball(right_pad_pos, LEFT)

    # Draw score
    score1_text = font.render(str(score_1), True, (255, 255, 255))
    score2_text = font.render(str(score_2), True, (255, 255, 255))
    canvas.blit(score1_text, (SCREEN_WIDTH/4,10))
    canvas.blit(score2_text, (3*SCREEN_WIDTH/4,10))

    pygame.display.update()
    fps_clock.tick(fps)