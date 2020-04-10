#!/usr/bin/env python3
from lib import *

def game_init() :

    global SURFACE_MAIN
    
    SURFACE_MAIN = pygame.display.set_mode( ( GAME_WIDTH, GAME_HEIGHT ) )

    pygame.display.set_caption( "rogue_like" )

def game_draw() :
    
    # Clear  surface
    SURFACE_MAIN.fill( COLOR_DEFAULT_BG )

    # Draw room
    #draw_room( level.get_room( player.get_room() )  )

    SURFACE_MAIN.blit( level.draw_room(), ( 0, 0 ) )
    # SURFACE_MAIN.blit( level.draw_minimap(), ( 0, 0 ) )

    # Draw minimap
    draw_minimap( level.get_room_map() )

    level.get_room_map()

    # Draw player
    player_position = player.get_tile()

    SURFACE_MAIN.blit( level.get_player_sprite(), ( player_position[0] * TILE_SIZE, player_position[1] * TILE_SIZE ) )
   
    # TODO: Draw UI
    


    # Update display
    pygame.display.update()

def get_minimap_sprite( room ) :
    sprite = MM_HIDDEN_SPRITE_16

    # Check if room exists
    if type( room ) == type( " " ):
        return sprite

    if room.get_coords() == player.get_room() :
        sprite = MM_CURRENT_SPRITE_16
        room.unhide()  
    elif not room.is_hidden() : 
        sprite = MM_VISIBLE_SPRITE_16
    elif room.is_discovered() :
        sprite = MM_UNKNOWN_SPRITE_16

    return sprite
    
def draw_minimap( room_map ) :
    # TODO: Get difficulty as size of mini map
    # TODO: Get offsets
    diff = 11
    xoff = 9*32 + 2
    yoff = 2

    # Find unknowns
    for y in range( 0, diff-1 ) :
        for x in range( 0, diff-1 ) :
            if not type( room_map[y][x] ) == type( " " ) and room_map[y][x].get_coords() == player.get_room() :
                for adj in room_map[y][x].get_adjacent() :
                    if adj == "L" and not type(room_map[y-1][x]) == type(" ") : room_map[y-1][x].discover()
                    if adj == "R" and not type(room_map[y+1][x]) == type(" ") : room_map[y+1][x].discover()
                    if adj == "T" and not type(room_map[y][x-1]) == type(" ") : room_map[y][x-1].discover()
                    if adj == "B" and not type(room_map[y][x+1]) == type(" ") : room_map[y][x+1].discover()

    # Draw minimap
    for x in range( 0, diff-1 ) :
        for y in range( 0, diff-1 ) :
            sprite = get_minimap_sprite( room_map[x][y] )
            SURFACE_MAIN.blit( sprite, ( x * MM_SIZE + xoff, y * MM_SIZE + yoff ) )


def game_main_loop() :

    while True :
        
        events = pygame.event.get()
        # Process events
        for event in events :
            if event.type == QUIT :
                pygame.quit()
                sys.exit()
            

            if event.type == pygame.KEYDOWN :

                if event.key == pygame.K_LEFT : level.move_player( -1, 0, "L" )
                if event.key == pygame.K_RIGHT : level.move_player( +1, 0, "R" )
                if event.key == pygame.K_UP   : level.move_player( 0, -1, "U" )
                if event.key == pygame.K_DOWN : level.move_player( 0, +1, "D" )
                
                game_draw()


def main() :
    
    pygame.init()
    
    global level
    global player
    global minimap

    player = Player( "Bob" )
    
    level = Level( player, 20 )
    #print( np.matrix( level.get_map() ) )

    game_init()
    game_main_loop()

if __name__ == '__main__' :
    main()