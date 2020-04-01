#!/usr/bin/env python3
from lib import *
from level import *

def game_init() :

    global SURFACE_MAIN
    
    SURFACE_MAIN = pygame.display.set_mode( ( GAME_WIDTH, GAME_HEIGHT ) )

    pygame.display.set_caption( "rouge_like" )

def game_draw() :
    
    # Clear  surface
    SURFACE_MAIN.fill( COLOR_DEFAULT_BG )

    # Draw map

    # Draw player
    SURFACE_MAIN.blit( PLAYER_SPRITE, ( 100, 100 ) )

    # Update display
    pygame.display.update()
    pygame.display.flip()

def game_main_loop() :

    while True :
        
        # Process events
        for event in pygame.event.get() :
            #print(event)
            if event.type == QUIT :
                pygame.quit()
                sys.exit()

        # Draw Game
        game_draw()

def main() :
    
    pygame.init()
    
    level = Level( 10 )
    print( np.matrix( level.get_map() ) )
    
    game_init()
    game_main_loop()

if __name__ == '__main__' :
    main()