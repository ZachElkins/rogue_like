#!/usr/bin/env python3
from lib import *

class Level :
    def __init__( self, player ) :
        # Size of level
        self.size = ( LEVEL_SIZE, LEVEL_SIZE )

        # 2D list of the map
        self.map = [[" "] * MAP_SIZE for _ in range( MAP_SIZE )]

        self.num_rooms = random.randint( 10, 30 )

        self.player = player

        # Generate level
        self.generate()
        self.reset_coords()
        self.check_edges()
        self.assign_layouts()
        self.set_room_map()
        self.distribute_keys()

    def generate( self ) :
        # Reset rooms
        self.room_coords = []

        self.keys = math.floor( self.num_rooms / 4 ) + random.randint( -1, 1 )

        # Create first room
        self.room_coords.append( ( random.randint( 0, self.size[0] ), random.randint( 0, self.size[1] ) ) )
        
        i = 0
        while i < self.num_rooms :
            room_options = []

            # For each room add all adjacent rooms and choose 1
            for room in self.room_coords :
                # Left
                if room[0] != 0 :
                    room_options.append( ( room[0]-1, room[1] ) )
                # Right
                if room[0] < self.size[0]-1 :
                    room_options.append( ( room[0]+1, room[1] ) )
                # Top
                if room[1] < self.size[1]-1 :
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
            self.map[coords[0]][coords[1]] = "#"

    def set_room_map( self ) :
        self.room_map = copy.deepcopy( self.map )
        for x in range( 0, len( self.room_map ) ) :
            for y in range( 0, len( self.room_map[0] ) ) :
                for room in self.rooms :
                    if room.get_coords() == ( x, y ):
                        self.room_map[x][y] = room

    def distribute_keys( self ) :
        for i in range( 0, self.keys ) :
            self.rooms[ random.randint (0, len( self.rooms )-1 ) ].give_key()


    def reset_coords( self ) :
        self.rooms = []
        self.room_coords = []
        for i in range( 0, self.size[0] ) :
            for j in range( 0, self.size[1] ) :
                if self.map[i][j] == "#" :
                    self.rooms.append( Room( ( i, j ) ) )
                    self.room_coords.append( ( i, j ) )

    def check_edges( self ) :
        for room in self.rooms :
            room.check_edges( self )
            room.check_adjacent( self )
            self.map[room.get_coords()[0]][room.get_coords()[1]] = f'[{room.get_num_edges()} | {room.get_num_adjacent()}]'

    def assign_layouts( self ) :
        room = random.randint( 0, len(self.rooms)-1 )

        # Starting room
        self.rooms[room].assign_layout( ROOMS["START"], "S" )

        self.start_room = self.rooms[room].get_coords()
        self.player.move_room( self.start_room )

        start_room_layout = self.rooms[room].get_layout()

        for x, row in enumerate( start_room_layout ) :
            for y, tile in enumerate( row ) :
                if start_room_layout[x][y] == ROOM_TAGS["PLAYER"] :
                    self.start_tile = ( x, y )
                    self.player.move_tile( self.start_tile, "D" )

        # Ending room
        final = False
        while not final :
            room = random.randint( 0, len(self.rooms)-1 )
            if not self.rooms[room].has_layout() :
                self.rooms[room].assign_layout( ROOMS["FINAL"], "F" )
                final = True

        for room in self.rooms :
            if not room.has_layout() :
                layout = random.randint( 0, len(ROOMS["MIDDLE"])-1 )
                room.assign_layout(  ROOMS["MIDDLE"][layout], "M" )

        for i in range( 0, self.size[0] ) :
            for j in range( 0, self.size[1] ) :
                if ( i , j ) in self.room_coords :
                    for room in self.rooms :
                        if room.get_coords() == ( i, j ) :
                            self.map[i][j] = room.get_room_type()
                else:
                    self.map[i][j] = " "

    def open_hatch( self ) :
        if self.player.keys() == self.num_keys :
            for room in self.rooms :
                if room.get_room_type() == "F" :
                    room.open_hatch()
    
    def get_num_keys( self ) :
        return self.keys

    def get_map( self ) :
        return self.map

    def get_room_coords( self ) :
        return self.room_coords
    
    def get_rooms( self ) :
        return self.rooms
    
    def get_size( self ) :
        return self.size
    
    def get_start_room( self ) :
        return self.start_room

    def get_start_tile( self ) :
        return self.start_tile
    
    def get_room( self, coords ) :
        for room in self.rooms :
            if room.get_coords() == coords :
                return room
    
    def get_room_map( self ) :
        return self.room_map
    
    def move_player( self, x, y, direction ) :
        curr_room = self.player.get_room()
        next_room = ( curr_room[0]+x, curr_room[1]+y )
    
        curr_tile = self.player.get_tile()
        next_tile = ( curr_tile[0]+x, curr_tile[1]+y )

        layout = self.get_room( curr_room ).get_layout()

        # Check for edge of map
        if -1 in next_tile or ROOMS["SIZE"] in next_tile : next_tile_type = ROOM_TAGS["FLOOR"]
        else : next_tile_type = ( layout[next_tile[1]][next_tile[0]] )

        # Check for walls
        if next_tile_type == "#" :
            return

        # Left
        if x < 0 :
            if next_tile[0] <= 0 :
                self.player.move_room( next_room )
                next_tile = ( ROOMS["SIZE"]-1, next_tile[1] )
        # Right
        if x > 0 :
            if next_tile[0] >= ROOMS["SIZE"]-1 :
                self.player.move_room( next_room )
                next_tile = ( 0, next_tile[1] )
        # Top
        if y < 0 :
            if next_tile[1] <= 0 :
                self.player.move_room( next_room )
                next_tile = ( next_tile[0], ROOMS["SIZE"]-1 )
        # Bottom
        if y > 0 :
            if next_tile[1] >= ROOMS["SIZE"]-1 :
                self.player.move_room( next_room )
                next_tile = ( next_tile[0], 0 )
        
        
        self.player.move_tile( next_tile, direction )

        self.get_room( curr_room ).draw_sprite()
        
        self.check_player_position()

    def check_player_position( self ) :
        # Check for keys
        player_tile = self.player.get_tile()
        curr_room = self.get_room( self.player.get_room() )
        key_tiles = curr_room.get_key_coords()
        
        if player_tile in key_tiles :
            self.player.pick_up( "KEY" )
            key_tiles.remove( player_tile )
            curr_room.draw_sprite()

    def draw_room( self ) :
        room = self.get_room( self.player.get_room() )
        return room.get_sprite()

    def get_player_sprite( self ) :
        return self.player.get_sprite()
