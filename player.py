from lib import *

class Player :
    
    def __init__( self ) :
        pass

class Wall :

    def __init__( self, x, y, size ) :
        pygame.sprite.Sprite.__init__( self )

        self.surface = pygame.surface( [size, size] )
        self.sprite = pygame.image.load( "./sprites/tiles/wall_01.png" ).convert_alpha()