from lib import *

class Player :
    
    def __init__( self, name ) :
        self.name = name

    def move_tile( self, tile ) :
        self.tile = tile
    
    def move_room( self, room) :
        self.room = room

    def move_level( self ) :
        pass

    def get_room( self ) :
        return self.room

    def get_tile( self ) :
        return self.tile
    
    def get_name( self ) :
        return self.name