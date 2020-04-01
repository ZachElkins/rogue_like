#!/usr/bin/env python3
from lib import *
from level import *
from layouts import *

global player_position

def game_init() :


    global SURFACE_MAIN
    
    SURFACE_MAIN = pygame.display.set_mode( ( GAME_WIDTH, GAME_HEIGHT ) )

    pygame.display.set_caption( "rouge_like" )

def game_draw( event ) :
    
    # Clear  surface
    SURFACE_MAIN.fill( COLOR_DEFAULT_BG )

    # Draw room
        # Get active room
        # Draw active room
    
    # Draw player
    # Draw UI
    
    # on mouse down
    if event == 5 :
        for room in level.get_rooms() :
            if room.get_room_type() == "S" :
                draw_room( room )


    # Update display
    pygame.display.update()
    pygame.display.flip()


def draw_room( room ) :
    layout = room.get_layout()
    size = room.get_size()

    for x in range( 0, size[0] ) :
        for y in range( 0, size[1] ) :
            tile = layout[x][y]
            if   tile == TAGS["WALL"] :
                sprite = WALL_SPRITE
            elif tile == TAGS["FLOOR"] :
                sprite = FLOOR_SPRITE
            elif tile == TAGS["ENEMY"] :
                sprite = ENEMY_SPRITE
            elif tile == TAGS["ITEM"] :
                sprite = ITEM_SPRITE
            elif tile == TAGS["PLAYER"] :
                sprite = FLOOR_SPRITE
                player_position = ( x, y )
            else : sprite = FLOOR_SPRITE
            SURFACE_MAIN.blit( sprite, ( x * TILE_SIZE, y * TILE_SIZE ) )

    SURFACE_MAIN.blit( PLAYER_SPRITE, ( player_position[0] * TILE_SIZE, player_position[1] * TILE_SIZE ) )


def game_main_loop() :

    while True :
        
        # Process events
        for event in pygame.event.get() :
            print(event.type)
            if event.type == QUIT :
                pygame.quit()
                sys.exit()


        if event.type == 5 :
            game_draw( 5 )

        # Draw Game
        #game_draw()

def main() :
    
    pygame.init()
    
    global level
    level = Level( 10 )
    print( np.matrix( level.get_map() ) )
    
    game_init()
    game_main_loop()

if __name__ == '__main__' :
    main()