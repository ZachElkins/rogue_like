from lib import *

# 16px Sprites
PLAYER_SPRITE_16 = pygame.image.load( "./sprites/player/playerx16.png" )
ENEMY_SPRITE_16 = pygame.image.load( "./sprites/enemies/sludge.png" )
WALL_SPRITE_16 = pygame.image.load( "./sprites/tiles/wall_01x16.png" )
KEY_SPRITE_16 = pygame.image.load( "./sprites/pickups/key.png" )
FLOOR_SPRITE_16 = pygame.image.load( "./sprites/tiles/floor_01x16.png" )
#ITEM_SPRITE_16 = pygame.image.load( "./sprites/tiles/floor_01x32.png" )

MM_HIDDEN_SPRITE_16 = pygame.image.load( "./sprites/minimap/hiddenx16.png" )
MM_VISIBLE_SPRITE_16 =  pygame.image.load( "./sprites/minimap/visiblex16.png" )
MM_CURRENT_SPRITE_16 =  pygame.image.load( "./sprites/minimap/currentx16.png" )
MM_UNKNOWN_SPRITE_16 =  pygame.image.load( "./sprites/minimap/unknownx16.png" )

# 32px Sprites
# PLAYER_SPRITE_32 = pygame.image.load( "./sprites/player/playerx32.png" )
# BAT_SPRITE_32 = pygame.image.load( "./sprites/enemies/batx32_01.png" )
# WALL_SPRITE_32 = pygame.image.load( "./sprites/tiles/wall_02x32.png" )
# KEY_SPRITE = pygame.image.load( "./sprites/pickups/key.png" )
# FLOOR_SPRITE_32 = pygame.image.load( "./sprites/tiles/floor_02x32.png" )
# STAIR_SPRITE_32 = pygame.image.load( "./sprites/tiles/stairs_01x32.png" )
# ITEM_SPRITE_32 = pygame.image.load( "./sprites/pickups/coinx32.png" )


PLAYER_SPRITE_UP = pygame.image.load( "./sprites/player/player_up.png" )
PLAYER_SPRITE_DOWN = pygame.image.load( "./sprites/player/player_down.png" )
PLAYER_SPRITE_LEFT = pygame.image.load( "./sprites/player/player_left.png" )
PLAYER_SPRITE_RIGHT = pygame.image.load( "./sprites/player/player_right.png" )

PLAYER_SPRITES = {
    "U" : pygame.image.load( "./sprites/player/player_up.png" ),
    "D" : pygame.image.load( "./sprites/player/player_down.png" ),
    "L" : pygame.image.load( "./sprites/player/player_left.png" ),
    "R" : pygame.image.load( "./sprites/player/player_right.png" )
}

FLOOR_SPRITES = []
FLOOR_SPRITES.extend( repeat( pygame.image.load( "./sprites/tiles/floor/floor_01.png" ), 2 ) )
FLOOR_SPRITES.extend( repeat( pygame.image.load( "./sprites/tiles/floor/floor_02.png" ), 2 ) )
FLOOR_SPRITES.extend( repeat( pygame.image.load( "./sprites/tiles/floor/floor_03.png" ), 2 ) )
FLOOR_SPRITES.extend( repeat( pygame.image.load( "./sprites/tiles/floor/floor_04.png" ), 2 ) )
FLOOR_SPRITES.extend( repeat( pygame.image.load( "./sprites/tiles/floor/floor_05.png" ), 86 ) )
FLOOR_SPRITES.extend( repeat( pygame.image.load( "./sprites/tiles/floor/floor_06.png" ), 2 ) )
FLOOR_SPRITES.extend( repeat( pygame.image.load( "./sprites/tiles/floor/floor_07.png" ), 2 ) )
FLOOR_SPRITES.extend( repeat( pygame.image.load( "./sprites/tiles/floor/floor_08.png" ), 2 ) )

WALL_SPRITES = [
    pygame.image.load( "./sprites/tiles/wall/wall_01.png" ),
    pygame.image.load( "./sprites/tiles/wall/wall_02.png" ),
    pygame.image.load( "./sprites/tiles/wall/wall_03.png" ),
    pygame.image.load( "./sprites/tiles/wall/wall_04.png" ),
    pygame.image.load( "./sprites/tiles/wall/wall_05.png" ),
    pygame.image.load( "./sprites/tiles/wall/wall_06.png" ),
    pygame.image.load( "./sprites/tiles/wall/wall_07.png" ),
    pygame.image.load( "./sprites/tiles/wall/wall_08.png" )
]

STAIR_SPRITE = pygame.image.load( "./sprites/tiles/stairs.png" )
HATCH_SPRITE = pygame.image.load( "./sprites/tiles/hatch.png" )