from lib import *

# Game Constants
GAME_WIDTH = 700
GAME_HEIGHT = 700

# Color Defenitions
COLOR_BEIGE = (204, 199, 157)
COLOR_BLACK = (0, 0, 0)

# Game Colors
COLOR_DEFAULT_BG = COLOR_BEIGE

# Sprites
PLAYER_SPRITE = pygame.image.load( "./sprites/player/player.png" )
ENEMY_SPRITE = pygame.image.load( "./sprites/enemies/sludge.png" )
WALL_SPRITE = pygame.image.load( "./sprites/tiles/wall_01.png" )
KEY_SPRITE = pygame.image.load( "./sprites/pickups/key.png" )