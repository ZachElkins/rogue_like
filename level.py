#!/usr/bin/env python3
from lib import *
from room import Room

class Level:
    def __init__( self, diff ) :
        # Size of level
        self.size = ( 0, 0 )
        # Difficulty of the level
        self.diff = diff
        # 2D list of the map
        self.map = [["[ ]"] * diff for _ in range(diff)]

        # Generate level
        self.generate()
        self.shrink_map()
        self.reset_coords()
        self.check_edges()

    def generate( self ) :

        # Reset rooms
        self.room_coords = []

        print( f'generating a new map (difficulty: {self.diff})' )

        # Create first room
        self.room_coords.append( ( random.randint( 0, self.diff-1 ), random.randint( 0, self.diff-1 ) ) )
        
        i = 0
        while i < self.diff :
            room_options = []

            # For each room add all adjacent rooms and choose 1
            for room in self.room_coords :
                # Left
                if room[0] != 0 :
                    room_options.append( ( room[0]-1, room[1] ) )
                # Right
                if room[0] < self.diff-1 :
                    room_options.append( ( room[0]+1, room[1] ) )
                # Top
                if room[1] < self.diff-1 :
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
            
        # Mark all rooms on the map
        for coords in self.room_coords :
            self.map[coords[0]][coords[1]] = 1

    def shrink_map( self ) :
        # Find empty rows
        empty_rows = []

        for i in range( 0, self.diff ) :
            is_empty = True
            j = 0
            while j < self.diff and is_empty :
                if ( i, j ) in self.room_coords :
                    # print(f'Row {i} is not empty, has value at ({i}, {j})')
                    is_empty = False
                j += 1
            if is_empty :
                empty_rows.append( i )

        # Remove empty rows
        for i in range( self.diff, -1, -1 ) :
            if i in empty_rows :
                del self.map[i]

        # Find empty columns
        empty_cols = []

        for j in range( 0, self.diff ) :
            is_empty = True
            i = 0
            while i < self.diff and is_empty :
                if ( i, j ) in self.room_coords :
                    # print(f'Row {i} is not empty, has value at ({i}, {j})')
                    is_empty = False
                i += 1
            if is_empty :
                empty_cols.append( j )

        for i in range( len( self.map )-1, -1, -1 ) :
            for j in range( self.diff, -1, -1 ) :
                if j in empty_cols :
                    del self.map[i][j]

        self.size = ( len(self.map), len(self.map[0]) )

        print(f'Reduced size:({self.diff},{self.diff}) => ({self.size[0]},{self.size[1]})')

    def reset_coords( self ) :
        self.rooms = []
        self.room_coords = []
        for i in range( 0, self.size[0] ) :
            for j in range( 0, self.size[1] ) :
                if self.map[i][j] == 1 :
                    self.rooms.append( Room( ( i, j ) ) )
                    self.room_coords.append( ( i, j ) )

                

    def check_edges( self ) :
        for room in self.rooms :
            room.check_edges( self )
            self.map[room.get_coords()[0]][room.get_coords()[1]] = f'[{room.get_num_edges()}]'

    def get_map( self ) :
        return self.map

    def get_room_coords( self ) :
        return self.room_coords
    
    def get_rooms( self ) :
        return self.rooms
    
    def get_size( self ) :
        return self.size
