from lib import *

class Enemy( Character ) :
    
    def __init__( self ) :
        super().__init__( "Skeleton", SKELETON_SPRITES, PLAYER_SOUNDS )
        self.moves_on = 2
        self.target_coords = ( 0, 0 )

    def set_target_coords( self, coords ) :
        self.target_coords = coords

    def get_moves_on( self ) :
        return self.moves_on

    def start_tile( self, tile ) :
        super().move_tile( tile, "D" )

    def move_tile( self, moves ) :
        if( moves % self.moves_on == 0 ) :
            super().move_tile( ( 0, 0) , self.get_next_move() )
    
    def get_next_move( self ) :
        m = ["L", "R", "U", "D"]
        return m[ random.randint( 0, len( m ) -1 ) ]