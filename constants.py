from lib import *

# Game Constants
GAME_WIDTH = 700
GAME_HEIGHT = 700

# Sizes (px)
TILE_SIZE = 32

# Color Defenitions
COLOR_BEIGE = (189, 176, 145)
COLOR_PURPLE = (103, 85, 98)
COLOR_BLACK = (0, 0, 0)

# Game Colors
COLOR_DEFAULT_BG = COLOR_BEIGE

# 16px Sprites
PLAYER_SPRITE_16 = pygame.image.load( "./sprites/player/playerx16.png" )
ENEMY_SPRITE_16 = pygame.image.load( "./sprites/enemies/sludge.png" )
WALL_SPRITE_16 = pygame.image.load( "./sprites/tiles/wall_01x16.png" )
KEY_SPRITE_16 = pygame.image.load( "./sprites/pickups/key.png" )
FLOOR_SPRITE_16 = pygame.image.load( "./sprites/tiles/floor_01x16.png" )

# 32px Sprites
PLAYER_SPRITE_32 = pygame.image.load( "./sprites/player/playerx32.png" )
# ENEMY_SPRITE = pygame.image.load( "./sprites/enemies/sludge.png" )
WALL_SPRITE_32 = pygame.image.load( "./sprites/tiles/wall_01x32.png" )
# KEY_SPRITE = pygame.image.load( "./sprites/pickups/key.png" )
FLOOR_SPRITE_32 = pygame.image.load( "./sprites/tiles/floor_01x32.png" )