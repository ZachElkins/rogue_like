#!/usr/bin/env python3
from lib import *
from level import *
from layouts import *

def game_init() :

    global SURFACE_MAIN
    
    SURFACE_MAIN = pygame.display.set_mode( ( GAME_WIDTH, GAME_HEIGHT ) )

    pygame.display.set_caption( "rouge_like" )

def game_draw( event ) :
    
    # Clear  surface
    SURFACE_MAIN.fill( COLOR_DEFAULT_BG )

    # Draw map
        # Get active room
        # Draw active room
    
    # on mouse down
    if event == 5 :
        for room in level.get_rooms() :
            if room.get_room_type() == "S" :
                draw_room( room )


    # Draw player
    # SURFACE_MAIN.blit( PLAYER_SPRITE, ( 100, 100 ) )
    # SURFACE_MAIN.blit( WALL_SPRITE, ( 120, 100 ) )
    # SURFACE_MAIN.blit( FLOOR_SPRITE, ( 120, 116 ) )
    # SURFACE_MAIN.blit( ENEMY_SPRITE, ( 140, 100 ) )
    # SURFACE_MAIN.blit( KEY_SPRITE, ( 160, 100 ) )

    # Update display
    pygame.display.update()
    pygame.display.flip()


def draw_room( room ) :
    layout = room.get_layout()
    size = room.get_size()

    for x in range( 0, size[0] ) :
        for y in range( 0, size[1] ) :
            tile = layout[x][y]
            if   tile == TAGS["WALL"] : sprite = WALL_SPRITE
            elif tile == TAGS["FLOOR"] : sprite = FLOOR_SPRITE
            elif tile == TAGS["ENEMY"] : sprite = ENEMY_SPRITE
            elif tile == TAGS["PLAYER"] : sprite = PLAYER_SPRITE
            elif tile == TAGS["PLAYER"] : sprite = PLAYER_SPRITE
            else : sprite = FLOOR_SPRITE
            SURFACE_MAIN.blit( sprite, ( x * TILE_SIZE, y * TILE_SIZE ) )


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