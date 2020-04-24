from lib import *

class Enemy( Character ) :
    
    def __init__( self, layout ) :
        super().__init__( "Skeleton", SKELETON_SPRITES, PLAYER_SOUNDS )
        self.moves_on = 2
        self.layout = layout
        self.next_move = ( -1, -1 )

    def set_target_coords( self, coords ) :
        self.target_coords = coords

    def get_moves_on( self ) :
        return self.moves_on

    def start_tile( self, tile ) :
        super().move_tile( tile, "D" )

    def move_tile( self, moves ) :
        if( moves % self.moves_on == 0 ) :
            self.get_next_move()
            m = ["L", "R", "U", "D"]
            d = m[ random.randint( 0, len( m ) -1 ) ]
            super().move_tile( self.next_move , d)
    
    def get_next_move( self ) :
        nodes = create_node_list( self.layout )
        path = bfs( nodes, self.tile, self.target_coords )
        if len( path ) <= 1 :
            print( 'NO PATH FOUND' )
            return
        self.next_move = path[1].get_coords()

class Node() :
    def __init__( self, coords ) :
        self.coords = coords
        self.adjacent = []
        self.visited = False

    def visit( self ) :
        self.visited = True

    def is_visited( self ) :
        return self.visited

    def get_coords( self ) :
        return self.coords
    
    def add_adjacent( self, node ) :
        self.adjacent.append( node )
    
    def get_adjacent( self ) :
        return self.adjacent

def create_node_list( layout ) :
    # TODO Enemies should not overlap!!!
    node_list = []
    for x in range( 0, len( layout ) - 1 ) :
        for y in range( 0, len( layout[x] ) - 1 )  :
            if not layout[y][x] == " " :
                continue
            node_list.append( Node( ( x, y ) ) )
    # Add edges
    for node1 in node_list :
        n1_coords = node1.get_coords()
        for node2 in node_list :
            n2_coords = node2.get_coords()
            adj = []
            adj.append( ( n1_coords[0] - 1, n1_coords[1] ) )
            adj.append( ( n1_coords[0] + 1, n1_coords[1] ) )
            adj.append( (n1_coords[0], n1_coords[1] - 1 ) )
            adj.append( (n1_coords[0], n1_coords[1] + 1 ) )
            if n2_coords in adj and not node1 == node2 :
                node1.add_adjacent( node2 )
        
    return node_list

def bfs( nodes, start_coords, end_coords ) :
    q = []

    start = nodes[0]

    for node in nodes :
        if node.get_coords() == start_coords :
            start = node
            q.append( [start] )
            continue

    start.visit()

    path = []

    max_attempts = 25000
    attempts = 0
    while q and attempts < max_attempts:
        path = q.pop( 0 )
        node = path[-1]

        if node.get_coords() == end_coords :
            return path
        
        for adjacent in node.get_adjacent() :
            new_path = copy.copy( path )
            new_path.append( adjacent )
            q.append( new_path )
        
        attempts+=1
    
    print( "MAX ATTEMPTS EXCEEDED" )
    return path