from lib import *

class Player :
    
    def __init__( self, room_coords, tile_coords ) :
        self.room = room_coords
        self.tile = tile_coords
        self.last_tile = (-1, -1)

    def move_tile( self, dir ) :

        self.last_tile = ( self.tile[0], self.tile[1] )

        # Left
        if dir == "L" :
            self.tile = ( self.tile[0]-1, self.tile[1] )
            if self.tile[0] == 0:
                self.room = ( self.room[0]-1, self.room[1] )
                self.tile = self.tile = (ROOMS["SIZE"]-1, self.tile[1] )
        # Right
        if dir == "R" :
            self.tile = ( self.tile[0]+1, self.tile[1] )
            if self.tile[0] == ROOMS["SIZE"]-1 :
                self.room = ( self.room[0]+1, self.room[1] )
                self.tile = self.tile = (0, self.tile[1] )
        # Up
        if dir == "U" :
            self.tile = ( self.tile[0], self.tile[1]-1 )
            if self.tile[1] == 0:
                self.room = ( self.room[0], self.room[1]-1 )
                self.tile = self.tile = (self.tile[0], ROOMS["SIZE"]-1 )
        # Down
        if dir == "D" :
            self.tile = ( self.tile[0], self.tile[1]+1 )
            if self.tile[1] == ROOMS["SIZE"]-1 :
                self.room = ( self.room[0], self.room[1]+1 )
                self.tile = self.tile = (self.tile[0], 0 )

    def move_room( self, dir ) :
        pass

    def move_level( self ) :
        pass

    def get_room( self ) :
        return self.room

    def get_tile( self ) :
        return self.tile
    
    def get_last_tile( self ) :
        return self.last_tile