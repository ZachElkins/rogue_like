from lib import *

class Dungeon :
    def __init__( self, player_name ) :
        self.player = Player( player_name )
        self.level = Level( self.player )
        self.draw_minimap()
        self.draw_room()
        self.level_number = 1
    
    def draw( self ) :
        self.draw_room()
        self.draw_minimap()

    def move_player( self, direction ) :
        if direction == "L" : move_coords = ( -1, 0 )
        if direction == "R" : move_coords = ( 1, 0 )
        if direction == "U" : move_coords = ( 0, -1 )
        if direction == "D" : move_coords = ( 0, 1 )
        
        self.level.move_player( move_coords[0], move_coords[1], direction ) 

    def draw_room( self ) :
        # Get room from level
        room_map = copy.copy( self.level.draw_room() )

        # Draw player
        player_pos = self.player.get_tile()
        room_map.blit( self.level.get_player_sprite(), ( player_pos[0] * TILE_SIZE, player_pos[1] * TILE_SIZE ) )

        # TODO: Draw enemies

        # TODO: Draw items

        # Save surface
        self.room_surface = room_map


    def draw_minimap( self ) :
        # TODO: Replace diff with some constant

        room_map = self.level.get_room_map()
        surface_size = MM_SIZE * LEVEL_SIZE

        self.minimap_surface = pygame.Surface( ( surface_size, surface_size ) )
        self.minimap_surface.fill( COLOR_PURPLE_05 ) 

        # Find unknowns
        for y in range( 0, LEVEL_SIZE ) :
            for x in range( 0, LEVEL_SIZE ) :
                if not type( room_map[y][x] ) == type( " " ) and room_map[y][x].get_coords() == self.player.get_room() :
                    for adj in room_map[y][x].get_adjacent() :
                        if adj == "L" and not type(room_map[y-1][x]) == type(" ") : room_map[y-1][x].discover()
                        if adj == "R" and not type(room_map[y+1][x]) == type(" ") : room_map[y+1][x].discover()
                        if adj == "T" and not type(room_map[y][x-1]) == type(" ") : room_map[y][x-1].discover()
                        if adj == "B" and not type(room_map[y][x+1]) == type(" ") : room_map[y][x+1].discover()

        # Draw minimap
        for y in range( 0, LEVEL_SIZE ) :
            for x in range( 0, LEVEL_SIZE ) :
                sprite = get_minimap_sprite( room_map[x][y], self.player.get_room() )
                self.minimap_surface.blit( sprite, ( x * MM_SIZE, y * MM_SIZE ) )

    def get_room_surface( self ) :
        return self.room_surface

    def get_minimap_surface( self ) :
        return self.minimap_surface
    
    def get_level_number( self ) :
        return self.level_number
    
    def get_player_name( self ) :
        return self.player.get_name()


def get_minimap_sprite( room, player_coords ) :
    sprite = pygame.Surface( ( 16, 16 ) )

    sprite.blit( MM_HIDDEN_SPRITE, ( 0, 0 ) )

    # Check if room exists
    if type( room ) == type( " " ):
        return sprite

    if room.get_coords() == player_coords :
        sprite.blit( MM_VISIBLE_SPRITE, ( 0, 0 ) )
        sprite.blit( MM_CURRENT_SPRITE, ( 0, 0 ) )
        room.unhide()  
    elif not room.is_hidden() :
        sprite.blit( MM_VISIBLE_SPRITE, ( 0, 0 ) )
    elif room.is_discovered() :
        sprite.blit( MM_UNKNOWN_SPRITE, ( 0, 0 ) )

    return sprite