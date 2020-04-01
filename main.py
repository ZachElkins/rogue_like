#!/usr/bin/env python3
from lib import *
from level import *
from layouts import *
from player import *

def game_init() :

    global SURFACE_MAIN
    global room_drawn
    room_drawn = False
    
    SURFACE_MAIN = pygame.display.set_mode( ( GAME_WIDTH, GAME_HEIGHT ) )

    pygame.display.set_caption( "rouge_like" )

def game_draw(  ) :
    
    # Clear  surface
    SURFACE_MAIN.fill( COLOR_DEFAULT_BG )

    # Draw room
        # Get active room
        # Draw active room
    for room in level.get_rooms() :
        if room.get_room_type() == "S" :
            draw_room( room )
    
    # Draw player
    player_position = player.get_tile()
    SURFACE_MAIN.blit( PLAYER_SPRITE_32, ( player_position[0] * TILE_SIZE, player_position[1] * TILE_SIZE ) )
    # Draw UI
    


    # Update display
    pygame.display.update()
    pygame.display.flip()

def get_sprite( tile ) :
    if   tile == TAGS["WALL"]   : sprite = WALL_SPRITE_32
    elif tile == TAGS["FLOOR"]  : sprite = FLOOR_SPRITE_32
    elif tile == TAGS["ENEMY"]  : sprite = ENEMY_SPRITE_16
    elif tile == TAGS["ITEM"]   : sprite = ITEM_SPRITE_16
    elif tile == TAGS["PLAYER"] : sprite = FLOOR_SPRITE_32
    else : sprite = FLOOR_SPRITE

    return sprite

def draw_room( room ) :
    layout = room.get_layout()
    size = room.get_size()

    for x in range( 0, size[0] ) :
        for y in range( 0, size[1] ) :
            tile = layout[x][y]
            sprite = get_sprite(tile)
            SURFACE_MAIN.blit( sprite, ( x * TILE_SIZE, y * TILE_SIZE ) )


def game_main_loop() :

    while True :
        
        events = pygame.event.get()
        # Process events
        for event in events :
            if event.type == QUIT :
                pygame.quit()
                sys.exit()
            
            if event.type == pygame.KEYDOWN :
                if event.key == pygame.K_LEFT : player.move_tile( "L" )
                if event.key == pygame.K_RIGHT : player.move_tile( "R" )
                if event.key == pygame.K_UP : player.move_tile( "U" )
                if event.key == pygame.K_DOWN : player.move_tile( "D" )

                game_draw()


        # Draw Game

def main() :
    
    pygame.init()
    
    global level
    global player

    level = Level( 10 )
    print( np.matrix( level.get_map() ) )

    player = Player( level.get_start_room(), level.get_start_tile() )

    print( player.get_tile() )
    
    game_init()
    game_main_loop()

if __name__ == '__main__' :
    main()