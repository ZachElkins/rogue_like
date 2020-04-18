#!/usr/bin/env python3
from lib import *

def game_init( game ) :

    global SURFACE_MAIN
    
    SURFACE_MAIN = pygame.display.set_mode( ( GAME_WIDTH, GAME_HEIGHT ) )

    pygame.display.set_caption( "rogue_like" )

def game_draw( game ) :
    
    # Clear  surface
    SURFACE_MAIN.fill( COLOR_DEFAULT_BG )

    SURFACE_MAIN.blit( game.get_room_surface(), ( 0, 0 ) )

    SURFACE_MAIN.blit( game.get_minimap_surface(), MM_OFFSET )

    # TODO: Draw UI
    name_text = TITLE_FONT.render( game.get_player_name(), 0, COLOR_PURPLE_04, None )
    SURFACE_MAIN.blit( name_text, ( MM_OFFSET[1], MM_OFFSET[0] ) )
    
    level_text = TEXT_FONT.render( f'Level {game.get_level_number()}', 0, COLOR_PURPLE_03, None )
    SURFACE_MAIN.blit( level_text, ( MM_OFFSET[1], MM_OFFSET[0] + 32 ) )
    
    keys_text = TEXT_FONT.render( f'Keys {game.get_keys_collected()}/{game.get_keys_total()}', 0, COLOR_PURPLE_03, None )
    SURFACE_MAIN.blit( keys_text, ( MM_OFFSET[1], MM_OFFSET[0] + 48 ) )

    # Update display
    pygame.display.update()


def game_main_loop( game ) :
    key_released = True

    while True :
        
        events = pygame.event.get()

        # Process events
        for event in events :
            if event.type == QUIT :
                pygame.quit()
                sys.exit()
            
        update_game = False
        if event.type == pygame.KEYDOWN and key_released :

            if event.key == pygame.K_LEFT :
                game.move_player( "L" )
                update_game = True
            if event.key == pygame.K_RIGHT :
                game.move_player( "R" )
                update_game = True
            if event.key == pygame.K_UP :
                game.move_player( "U" )
                update_game = True
            if event.key == pygame.K_DOWN :
                game.move_player( "D" )
                update_game = True

            if update_game  :
                game.draw()
                game_draw( game )
                key_released = False
                
        elif event.type == pygame.KEYUP :
            key_released = True

def main() :
    
    pygame.init()

    player_name = "Player Name"

    game = Dungeon( player_name )

    game_init( game )
    game_main_loop( game )

if __name__ == '__main__' :
    main()