#!/usr/bin/env python3
from lib import *
from level import *
import pygame, sys
from pygame.locals import *

def start_game():
    pygame.init()
    DISPALYSURF = pygame.display.set_mode( ( 750, 750 ) )
    pygame.display.set_caption( "rouge_like" )
    while True :
        for event in pygame.event.get() :
            print(event)
            if event.type == QUIT :
                pygame.quit()
                sys.exit()

def main() :
    level = Level( 10 )
    print( np.matrix( level.get_map() ) )
    start_game()

if __name__ == '__main__' :
    main()