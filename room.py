from lib import *

class Room :
    def __init__( self, coords ) :
        self.coords = coords
        self.edges = []
        self.adjacent = []
        self.layout = []
        self.hidden = True
        self.discovered = False

    def check_adjacent( self, level ) :
        self.num_adjacent = 0

        room_coords = level.get_room_coords()
        level_size = level.get_size()

        # Left
        if ( self.coords[0]-1, self.coords[1] ) in room_coords and not self.coords[0] == 0 :
            self.num_adjacent += 1
            self.adjacent.append( "L" )
        # Right
        if ( self.coords[0]+1, self.coords[1] ) in room_coords and not self.coords[0] == level_size[1]-1 :
            self.num_adjacent += 1
            self.adjacent.append( "R" )
        # Top
        if ( self.coords[0], self.coords[1]-1 ) in room_coords and not self.coords[1] == 0 :
            self.num_adjacent += 1
            self.adjacent.append( "T" )
        # Bottom
        if ( self.coords[0], self.coords[1]+1 ) in room_coords and not self.coords[1] == level_size[0]-1 :
            self.num_adjacent += 1
            self.adjacent.append( "B" )

    
    def check_edges( self, level ) :
        self.num_edges = 0

        room_coords = level.get_room_coords()
        level_size = level.get_size()

        # Left
        if ( self.coords[0]-1, self.coords[1] ) not in room_coords or self.coords[0] == 0 :
            self.num_edges += 1
            self.edges.append( "L" )
        # Right
        if ( self.coords[0]+1, self.coords[1] ) not in room_coords or self.coords[0] == LEVEL_SIZE :
            self.num_edges += 1
            self.edges.append( "R" )
        # Top
        if ( self.coords[0], self.coords[1]-1 ) not in room_coords or self.coords[1] == 0 :
            self.num_edges += 1
            self.edges.append( "T" )
        # Bottom
        if ( self.coords[0], self.coords[1]+1 ) not in room_coords or self.coords[1] == LEVEL_SIZE :
            self.num_edges += 1
            self.edges.append( "B" )
    
    def get_num_edges( self ) :
        return self.num_edges

    def get_num_adjacent( self ) :
        return self.num_adjacent
    
    def get_adjacent( self ) :
        return self.adjacent

    def get_coords( self ) :
        return self.coords
    
    def assign_layout( self, layout, room_type ) :
        self.layout = copy.deepcopy(layout)
        self.room_type = room_type
        self.add_edges()
        self.draw_sprite()
        
    def add_edges( self ) :

        layout_size = len( self.layout )

        # Left
        if "L" in self.edges :
            for i in range( 0, layout_size ) :
                self.layout[i][0] = ROOM_TAGS["WALL"]
        # Right
        if "R" in self.edges :
            for i in range( 0, layout_size ) :
                self.layout[i][layout_size-1] = ROOM_TAGS["WALL"]
        # Top
        if "T" in self.edges :
            for j in range( 0, layout_size ) :
                self.layout[0][j] = ROOM_TAGS["WALL"]
        # Bottom
        if "B" in self.edges :
            for j in range( 0, layout_size ) :
                self.layout[layout_size-1][j] = ROOM_TAGS["WALL"]

    
    def has_layout( self ) :
        return not self.layout == []

    def get_layout( self ) :
        return self.layout
    
    def get_room_type( self ) :
        return self.room_type
    
    def get_size( self ) :
        return ( len(self.layout) , len(self.layout[0]) )

    def print_data( self ) :
        print(f'Coords: {self.coords} \nEdges: ({self.num_edges}) {self.edges} \nAdjacent: ({self.num_adjacent}) {self.adjacent}')
        print("========================")

    def is_hidden( self ) :
        return self.hidden
        
    def unhide( self ) :
        self.hidden = False
    
    def discover( self ) :
        self.discovered = True

    def is_discovered( self ) :
        return self.discovered
    
    def draw_sprite( self ) :
        
        surface_size = TILE_SIZE * ROOMS["SIZE"]
        
        self.sprite = pygame.Surface( ( surface_size, surface_size ) )
        self.sprite.fill( COLOR_PURPLE_05 )

        size = self.get_size()
        layout = self.get_layout()

        for y in range( 0, size[0] ) :
            for x in range( 0, size[1] ) :
                tile = layout[y][x]
                sprite = get_tile_sprite( tile )
                self.sprite.blit( sprite, ( x * TILE_SIZE, y * TILE_SIZE ) )

    def get_sprite( self ) :
        return self.sprite


def get_tile_sprite( tile ) :
    if   tile == ROOM_TAGS["WALL"]   : sprite = WALL_SPRITE_32
    elif tile == ROOM_TAGS["STAIRS"] : sprite = STAIR_SPRITE_32
    else : sprite = FLOOR_SPRITES[random.randint(0, len( FLOOR_SPRITES )-1 )]

    return sprite