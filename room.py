from lib import *

class Room:
    def __init__( self, coords ) :
        self.coords = coords
        self.edges = []
        self.adjacent = []
        self.layout = []

    def check_adjacent( self, level ) :
        self.num_adjacent = 0

        room_coords = level.get_room_coords()
        level_size = level.get_size()

        # Left
        if ( self.coords[0], self.coords[1]-1 ) in room_coords and not self.coords[1] == 0 :
            self.num_adjacent += 1
            self.adjacent.append( "L" )
        # Right
        if ( self.coords[0], self.coords[1]+1 ) in room_coords and not self.coords[1] == level_size[1]-1 :
            self.num_adjacent += 1
            self.adjacent.append( "R" )
        # Top
        if ( self.coords[0]-1, self.coords[1] ) in room_coords and not self.coords[0] == 0 :
            self.num_adjacent += 1
            self.adjacent.append( "T" )
        # Bottom
        if ( self.coords[0]+1, self.coords[1] ) in room_coords and not self.coords[0] == level_size[0]-1 :
            self.num_adjacent += 1
            self.adjacent.append( "B" )

    
    def check_edges( self, level ) :
        self.num_edges = 0

        room_coords = level.get_room_coords()
        level_size = level.get_size()

        # Left
        if ( self.coords[0], self.coords[1]-1 ) not in room_coords or self.coords[1] == 0 :
            self.num_edges += 1
            self.edges.append( "L" )
        # Right
        if ( self.coords[0], self.coords[1]+1 ) not in room_coords or self.coords[1] == level_size[1]-1 :
            self.num_edges += 1
            self.edges.append( "R" )
        # Top
        if ( self.coords[0]-1, self.coords[1] ) not in room_coords or self.coords[0] == 0 :
            self.num_edges += 1
            self.edges.append( "T" )
        # Bottom
        if ( self.coords[0]+1, self.coords[1] ) not in room_coords or self.coords[0] == level_size[0]-1 :
            self.num_edges += 1
            self.edges.append( "B" )
    
    def get_num_edges( self ) :
        return self.num_edges

    def get_num_adjacent( self ) :
        return self.num_adjacent

    def get_coords( self ) :
        return self.coords
    
    def assign_layout( self, layout, room_type ) :
        self.layout = layout
        self.room_type = room_type
    
    def has_layout( self ) :
        return not self.layout == []

    def get_layout( self ) :
        return self.layout
    
    def get_room_type( self ) :
        return self.room_type

    def print_data( self ) :
        print(f'Coords: {self.coords} \nEdges: ({self.num_edges}) {self.edges} \nAdjacent: ({self.num_adjacent}) {self.adjacent}')
        print("========================")