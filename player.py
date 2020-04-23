from lib import *

class Player( Character ) :
    
    def __init__( self, name ) :
        super().__init__( "Player", PLAYER_SPRITES, PLAYER_SOUNDS )
        self.name = name
        self.keys = 0
        self.level = 1

    def move_level( self ) :
        self.keys = 0
        self.level += 1
    
    def get_level( self ) :
        return self.level
    
    def get_name( self ) :
        return self.name

    def get_num_keys( self ) :
        return self.keys 
    
    def pick_up( self, item ) :
        if item == "KEY" :
            self.keys += 1
            pygame.mixer.music.load( PICKUP_SOUNDS["KEY"] )
            pygame.mixer.music.play( 1 )
            