from lib import *

PLAYER_SPRITES = {
    "U" : pygame.image.load( "./sprites/player/player_up.png" ),
    "D" : pygame.image.load( "./sprites/player/player_down.png" ),
    "L" : pygame.image.load( "./sprites/player/player_left.png" ),
    "R" : pygame.image.load( "./sprites/player/player_right.png" )
}

SKELETON_SPRITES = {
    "U" : pygame.image.load( "./sprites/enemies/skeleton/skeleton_up.png" ),
    "D" : pygame.image.load( "./sprites/enemies/skeleton/skeleton_down.png" ),
    "L" : pygame.image.load( "./sprites/enemies/skeleton/skeleton_left.png" ),
    "R" : pygame.image.load( "./sprites/enemies/skeleton/skeleton_right.png" )
}

ITEM_SPRITES = {
    "key"   : pygame.image.load( "./sprites/pickups/key.png" ),
    "potion": pygame.image.load( "./sprites/pickups/potion.png" ),
    "coin"  : pygame.image.load( "./sprites/pickups/coin.png" ),
    "bomb"  : pygame.image.load( "./sprites/pickups/bomb.png" ),
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

STAIR_SPRITE = pygame.image.load( "./sprites/tiles/stairs.png" )
HATCH_SPRITE = pygame.image.load( "./sprites/tiles/hatch.png" )

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

MM_HIDDEN_SPRITE = pygame.image.load( "./sprites/minimap/hidden.png" )
MM_VISIBLE_SPRITE =  pygame.image.load( "./sprites/minimap/visible.png" )
MM_CURRENT_SPRITE =  pygame.image.load( "./sprites/minimap/current.png" )
MM_UNKNOWN_SPRITE =  pygame.image.load( "./sprites/minimap/unknown.png" )
