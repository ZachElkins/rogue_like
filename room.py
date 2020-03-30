from lib import *

class Room:
    def __init__(self, coords):
        self.coords = coords
        self.edges = []
    
    def check_edges(self, level):
        self.num_edges = 0

        # Left
        if ( self.coords[0]-1, self.coords[1] ) in level.get_rooms() or self.coords[0] == 0:
            self.num_edges += 1
            self.edges.append( "L" )
        # Right
        if ( self.coords[0]+1, self.coords[1] ) in level.get_rooms() or self.coords[0] == level.get_size()-1:
            self.num_edges += 1
            self.edges.append( "R" )
        # Top
        if ( self.coords[0], self.coords[1]-1 ) in level.get_rooms() or self.coords[1] == 0:
            self.num_edges += 1
            self.edges.append( "T" )
        # Botttom
        if ( self.coords[0], self.coords[1]+1 ) in level.get_rooms() or self.coords[1] == level.get_size()-1:
            self.num_edges += 1
            self.edges.append(" B ")