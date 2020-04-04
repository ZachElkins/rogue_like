from lib import *

class Player :
    
    def __init__( self, name ) :
        self.name = name

    def move_tile( self, tile ) :
        print( f'TILE: ({tile[0]}, {tile[1]})' )
        self.tile = tile
    
    def move_room( self, room) :
        print( f'TILE: ({room[0]}, {room[1]})' )
        self.room = room

    def move_level( self ) :
        pass

    def get_room( self ) :
        return self.room

    def get_tile( self ) :
        return self.tile