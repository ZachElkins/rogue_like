from lib import *

class Room :
    def __init__( self, coords ) :
        self.coords = coords
        self.edges = []
        self.adjacent = []
        self.layout = []
        self.hidden = True
        self.discovered = False
        self.closed = True
        self.keys = []

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
        self.draw_base_sprite()
    
    def get_free_tiles( self ) :
        size = self.get_size()
        layout = self.get_layout()

        free_tiles = ( size[0] - 2 ) * ( size[1] - 2 )
        for x in range( 1, size[0]-3 ) :
            for y in range( 1, size[1]-3 ) :
                if layout[x][y] in self.keys :
                    free_tiles -= 1
                elif layout[y][x] == ROOM_TAGS["WALL"] :
                    free_tiles -= 1
        
        return free_tiles
        
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

    def give_key( self ) : 
        
        if self.get_free_tiles() <= 0 or self.room_type != "M" :
            return False

        size = self.get_size()
        layout = self.get_layout()

        tile_found = False
        while not tile_found :
            # Keys won't spawn on edges
            x = random.randint( 1, size[0]-2 )
            y = random.randint( 1, size[1]-2 )
            if layout[y][x] == ROOM_TAGS["FLOOR"] and ( x, y ) not in self.keys :
                self.keys.append( (x, y) )
                tile_found = True
                self.draw_sprite()
                return True
                    
    def get_key_coords( self ) :
        return self.keys

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
    
    def open_hatch( self ) :
        self.closed = False

    def is_discovered( self ) :
        return self.discovered
    
    def get_stairs_coords( self ) :
        size = self.get_size()
        layout = self.get_layout()
        
        if self.room_type != "F" :
            return False
        
        for y in range( 0, size[0] ) :
            for x in range( 0, size[1] ) :
                if layout[y][x] == ROOM_TAGS["STAIRS"] :
                    return ( x, y )
    
    def draw_base_sprite( self ) :
        
        surface_size = TILE_SIZE * ROOMS["SIZE"]
        
        self.base_sprite = pygame.Surface( ( surface_size, surface_size ) )
        self.base_sprite.fill( COLOR_PURPLE_05 )

        size = self.get_size()
        layout = self.get_layout()

        for y in range( 0, size[0] ) :
            for x in range( 0, size[1] ) :
                tile = layout[y][x]
                sprite = get_tile_sprite( tile )
                self.base_sprite.blit( sprite, ( x * TILE_SIZE, y * TILE_SIZE ) )

        self.sprite = copy.copy( self.base_sprite )

    def draw_sprite( self ) :
        size = self.get_size()
        layout = self.get_layout()
        self.sprite = copy.copy( self.base_sprite )

        # Draw keys
        for x in range( 0, size[0] ) :
            for y in range( 0, size[1] ) :
                if ( x, y ) in self.keys :
                    self.sprite.blit( ITEM_SPRITES["KEY"],( x * TILE_SIZE, y * TILE_SIZE ) )

        if self.get_stairs_coords() and not self.closed :
            self.sprite.blit( STAIR_SPRITE, ( self.get_stairs_coords()[0] * TILE_SIZE, self.get_stairs_coords()[1] * TILE_SIZE ) )
        # if self.room_type == "F" and not self.closed :
            # for y in range( 0, size[0] ) :
            #     for x in range( 0, size[1] ) :
            #         if layout[y][x] == ROOM_TAGS["STAIRS"] : 
            #             self.sprite.blit( STAIR_SPRITE,  ( x * TILE_SIZE, y * TILE_SIZE ) )

    def get_sprite( self ) :
        return self.sprite

def get_tile_sprite( tile ) :
    if tile == ROOM_TAGS["WALL"]     : sprite = WALL_SPRITES[random.randint(0, len( WALL_SPRITES )-1 )]
    elif tile == ROOM_TAGS["STAIRS"] : sprite = HATCH_SPRITE
    else :  sprite = FLOOR_SPRITES[random.randint(0, len( FLOOR_SPRITES )-1 )]

    return sprite