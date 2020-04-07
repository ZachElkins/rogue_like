from lib import *

class Dungeon :
    def __init__( self, player, diff ) :
        self.level = Level( diff )
    
    def draw( self ) :
        pass