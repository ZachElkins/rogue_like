from lib import *

class Room:
    def __init__( self, coords ) :
        self.coords = coords
        self.edges = []
    
    def check_edges( self, level ) :
        self.num_edges = 0

        room_coords = level.get_room_coords()
        level_size = level.get_size()

        # Left
        if ( self.coords[0], self.coords[1]-1 ) in room_coords or self.coords[1] == 0 :
            self.num_edges += 1
            self.edges.append(" L ")
        # Right
        if ( self.coords[0], self.coords[1]+1 ) in room_coords or self.coords[1] == level_size-1 :
            self.num_edges += 1
            self.edges.append( "R" )
        # Top
        if ( self.coords[0]-1, self.coords[1] ) in room_coords or self.coords[0] == 0 :
            self.num_edges += 1
            self.edges.append( "T" )
        # Bottom
        if ( self.coords[0]+1, self.coords[1] ) in room_coords or self.coords[0] == level_size-1 :
            self.num_edges += 1
            self.edges.append( "B" )
    
    def get_num_edges( self ) :
        return self.num_edges

    def get_coords( self ) :
        return self.coords
    
    def print_data( self ) :
        print(f'Coords: {self.coords} \nEdges: ({self.num_edges}) {self.edges}')
        print("========================")