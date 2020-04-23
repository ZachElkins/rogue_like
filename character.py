from lib import *

class Character :
    
    def __init__( self, type, sprites, sounds ) :
        self.sprites = sprites
        self.sounds = sounds

    def move_tile( self, tile, direction ) :
        self.tile = tile
        self.current_sprite = self.sprites[direction]
        pygame.mixer.music.load( self.sounds["MOVEMENT"][ random.randint( 0, len( self.sounds["MOVEMENT"] )-1 ) ] )
        pygame.mixer.music.play( 1 )
        
    def move_room( self, room ) :
        self.room = room

    def get_tile( self ) :
        return self.tile

    def get_room( self ) :
        return self.room
    
    def get_sprite( self ) :
        return self.current_sprite