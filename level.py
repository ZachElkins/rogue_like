#!/usr/bin/env python3
from lib import *
from room import Room

class Level:
    def __init__( self, diff ) :
        # Size of the level
        self.size = diff
        # Difficulty of the level
        self.diff = diff
        # 2D list of the map
        self.map = [["[ ]"] * diff for _ in range(diff)]
        # Coordinates of every room
        self.room_coords = []
        # Room objects
        self.rooms = []

        #generate room
        self.generate()

    def generate( self ) :

        # Reset rooms
        self.room_coords = []

        print( f'generating a new map (difficulty: {self.diff})' )

        # Create first room
        self.room_coords.append( ( random.randint( 0, self.size-1 ), random.randint( 0, self.size-1 ) ) )
        
        i = 0
        while i < self.diff :
            room_options = []

            # For each room add all adjacent rooms and choose 1
            for room in self.room_coords :
                # Left
                if room[0] != 0 :
                    room_options.append( ( room[0]-1, room[1] ) )
                # Right
                if room[0] < self.size-1 :
                    room_options.append( ( room[0]+1, room[1] ) )
                # Top
                if room[1] < self.size-1 :
                    room_options.append( ( room[0], room[1]+1 ) )
                # Bottom
                if room[1] != 0 :
                    room_options.append( ( room[0], room[1]-1 ) )

                # Randomly choose a room
                new_room = room_options[random.randint( 0, len( room_options )-1 )]

            # Check if new room is a duplicates
            if not new_room in self.room_coords :
                self.room_coords.append( new_room )
                i += 1
            
        # Create room objects from room coordinates
        self.rooms = []
        for coords in self.room_coords :
            self.rooms.append( Room( coords ) )
        
        # Check all their edges
        for room in self.rooms :
            room.check_edges( self )
            self.map[room.get_coords()[0]][room.get_coords()[1]] = f'[{room.get_num_edges()}]'
            room.print_data()

    def get_map( self ) :
        return self.map

    def get_room_coords( self ) :
        return self.room_coords
    
    def get_rooms( self ) :
        return self.rooms
    
    def get_size( self ) :
        return self.size
