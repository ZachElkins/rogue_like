from lib import *

class Player :
    
    def __init__( self, name ) :
        self.name = name
        self.keys = 0

    def move_tile( self, tile, direction ) :
        self.tile = tile
        self.sprite = PLAYER_SPRITES[direction]
    
    def move_room( self, room ) :
        self.room = room

    def move_level( self ) :
        self.keys = 0

    def get_room( self ) :
        return self.room

    def get_tile( self ) :
        return self.tile
    
    def get_name( self ) :
        return self.name

    def get_num_keys( self ) :
        return self.keys 
    
    def pick_up( self, item ) :
        if item == "KEY" :
            self.keys += 1

    def get_sprite( self ) :
        return self.sprite