from lib import *

# Game Constants
GAME_WIDTH = 800
GAME_HEIGHT = 500

# Sizes (px)
TILE_SIZE = 32
MM_SIZE = 16

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
ITEM_SPRITE_16 = pygame.image.load( "./sprites/tiles/floor_01x32.png" )

MM_HIDDEN_SPRITE_16 = pygame.image.load( "./sprites/minimap/hiddenx16.png" )
MM_VISIBLE_SPRITE_16 =  pygame.image.load( "./sprites/minimap/visiblex16.png" )
MM_CURRENT_SPRITE_16 =  pygame.image.load( "./sprites/minimap/currentx16.png" )
MM_UNKNOWN_SPRITE_16 =  pygame.image.load( "./sprites/minimap/unknownx16.png" )

# 32px Sprites
PLAYER_SPRITE_32 = pygame.image.load( "./sprites/player/playerx32.png" )
# ENEMY_SPRITE = pygame.image.load( "./sprites/enemies/sludge.png" )
WALL_SPRITE_32 = pygame.image.load( "./sprites/tiles/wall_01x32.png" )
# KEY_SPRITE = pygame.image.load( "./sprites/pickups/key.png" )
FLOOR_SPRITE_32 = pygame.image.load( "./sprites/tiles/floor_01x32.png" )

# # : Walls
# P : Player
# E : Enemy
# I : Item
# S : Stairs
# T : Trap
# O : Oject

LEVEL_SIZE = 9

ROOM_TAGS = {
    "WALL" : "#",
    "PLAYER" : "P",
    "ENEMY": "E",
    "ITEM": "I",
    "STAIRS": "S",
    "TRAP": "T",
    "OBJECT": "O",
    "FLOOR": " "
}

MM_TAGS = {
    "ROOM" : "#",
    "EMPTY" : " "
}

ROOMS = {
    "START":[
        ["#", "#", "#", "#", " ", "#", "#", "#", "#"],
        ["#", " ", " ", " ", " ", " ", " ", " ", "#"],
        ["#", " ", "P", " ", " ", " ", " ", " ", "#"],
        ["#", " ", " ", " ", " ", " ", " ", " ", "#"],
        [" ", " ", " ", " ", " ", " ", " ", " ", " "],
        ["#", " ", " ", " ", " ", " ", " ", " ", "#"],
        ["#", " ", " ", " ", " ", " ", " ", " ", "#"],
        ["#", " ", " ", " ", " ", " ", " ", " ", "#"],
        ["#", "#", "#", "#", " ", "#", "#", "#", "#"]
    ],
    "MIDDLE": [
        [
        ["#", "#", "#", "#", " ", "#", "#", "#", "#"],
        ["#", "#", " ", " ", " ", " ", " ", " ", "#"],
        ["#", " ", " ", " ", "#", " ", " ", " ", "#"],
        ["#", " ", " ", " ", "#", "#", " ", " ", "#"],
        [" ", " ", " ", " ", "#", " ", "#", " ", " "],
        ["#", " ", " ", " ", "#", " ", " ", " ", "#"],
        ["#", " ", " ", " ", "#", " ", " ", " ", "#"],
        ["#", " ", " ", " ", " ", " ", " ", " ", "#"],
        ["#", "#", "#", "#", " ", "#", "#", "#", "#"]
        ],
        [
        ["#", "#", "#", "#", " ", "#", "#", "#", "#"],
        ["#", " ", " ", " ", " ", " ", "O", "O", "#"],
        ["#", " ", " ", "#", " ", " ", "E", "O", "#"],
        ["#", " ", " ", "#", " ", " ", " ", " ", "#"],
        [" ", " ", "I", "#", " ", " ", " ", " ", " "],
        ["#", " ", " ", "#", " ", " ", " ", " ", "#"],
        ["#", " ", " ", "#", " ", " ", " ", " ", "#"],
        ["#", " ", " ", " ", " ", " ", " ", " ", "#"],
        ["#", "#", "#", "#", " ", "#", "#", "#", "#"]
        ],
        [
        ["#", "#", "#", "#", " ", "#", "#", "#", "#"],
        ["#", "E", " ", " ", " ", " ", " ", "E", "#"],
        ["#", " ", " ", " ", "#", " ", " ", " ", "#"],
        ["#", " ", " ", " ", " ", " ", " ", " ", "#"],
        [" ", " ", "#", " ", "I", " ", "#", " ", " "],
        ["#", " ", " ", " ", " ", " ", " ", " ", "#"],
        ["#", " ", " ", " ", "#", " ", " ", " ", "#"],
        ["#", " ", " ", " ", " ", " ", " ", " ", "#"],
        ["#", "#", "#", "#", " ", "#", "#", "#", "#"]
        ],
        [
        ["#", "#", "#", "#", " ", "#", "#", "#", "#"],
        ["#", " ", " ", " ", " ", " ", " ", "I", "#"],
        ["#", " ", " ", " ", " ", " ", " ", " ", "#"],
        ["#", " ", " ", "#", "#", "#", " ", " ", "#"],
        [" ", " ", " ", " ", "E", " ", " ", " ", " "],
        ["#", " ", " ", "#", "#", "#", " ", " ", "#"],
        ["#", " ", " ", " ", " ", " ", " ", " ", "#"],
        ["#", "I", " ", " ", " ", " ", " ", " ", "#"],
        ["#", "#", "#", "#", " ", "#", "#", "#", "#"]
        ]
    ],

    "FINAL": [
        ["#", "#", "#", "#", " ", "#", "#", "#", "#"],
        ["#", " ", " ", " ", " ", " ", " ", " ", "#"],
        ["#", " ", "#", "#", "#", "#", "#", " ", "#"],
        ["#", " ", "#", " ", " ", " ", "#", " ", "#"],
        [" ", " ", "#", " ", "#", " ", "#", " ", " "],
        ["#", " ", "#", " ", "#", "S", "#", " ", "#"],
        ["#", " ", "#", " ", "#", "#", "#", " ", "#"],
        ["#", " ", " ", " ", " ", " ", " ", " ", "#"],
        ["#", "#", "#", "#", " ", "#", "#", "#", "#"]
    ],
    
    "SIZE": 9
}