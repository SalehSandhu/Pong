import pygame

# Initialise all Pygame modules.
pygame.init()

# --------------------------------------------------
# GAME CONFIGURATION
# --------------------------------------------------

# Define the dimensions of the game window.
WIDTH, HEIGHT = 700, 500

# Create the game window and set its title.
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong")

# Set the game's frame rate to 60 frames per second.
FPS = 60

# Define the colours used throughout the game (RGB format).
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Define the dimensions of the paddles and the ball.
PADDLE_WIDTH, PADDLE_HEIGHT = 20, 100
BALL_RADIUS = 7

# Configure the font used to display scores and winning messages.
SCORE_FONT = pygame.font.SysFont("comicsans", 50)

# Number of points required for a player to win.
WINNING_SCORE = 10


# --------------------------------------------------
# PADDLE CLASS
# --------------------------------------------------

class Paddle:
    # Define the paddle's colour and movement speed.
    COLOR = WHITE
    VEL = 4

    def __init__(self, x, y, width, height):
        """
        Initialise a paddle with its starting position
        and dimensions.

        Store the original coordinates so the paddle
        can be reset after a game finishes.
        """
        self.x = self.origional_x = x
        self.y = self.origional_y = y
        self.width = width
        self.height = height

    def draw(self, win):
        """Draw the paddle as a rectangle on the game window."""
        pygame.draw.rect(
            win,
            self.COLOR,
            (self.x, self.y, self.width, self.height)
        )

    def move(self, up=True):
        """
        Move the paddle vertically.

        If up is True, move upwards by subtracting
        the paddle's velocity from its y-coordinate.

        Otherwise, move downwards by increasing
        its y-coordinate.
        """
        if up:
            self.y -= self.VEL