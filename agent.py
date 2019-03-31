from graph import *
import time
import sys
import random
import copy


##########################
#  Agent
##########################

def tcHuer( state):
	size = len(state)
	dist = 0
	num = 1
	for i  in range( size):
		for j in range( size):
			actual = find( state, num)
			dist += abs( actual[0] - i)
			dist += abs( actual[1] - j)

			num += 1
			if(num == size * size): 
				return dist


def inversions( x, lst):
	dist = 0
	for i in lst:
		if (i < x and i != 0 and x != 0):
			dist += 1

	return dist


def invHuer( state):
	size = len( state)
	merged = []
	for i in state:
		merged += i

	dist = 0
	ln = len(merged)
	for i in range( ln):	
		curr = merged[i]
		dist += inversions( curr, merged[i+1:])
	return dist



def huer( state):
	return invHuer(state) + tcHuer( state)/5



def getKey( state):
    key = []
    for i in state:
        for j in i:
            key.append(j)
    return str( key).strip('[]')


def numToWord( n):
    if(n == 0): 
        return 'up'
    elif(n == 1): 
        return 'down'
    elif(n == 2):
        return 'left'
    else:
        return 'right'
 

def printBoard( state):
	print
	for i in range( len(state)):
		for j in range( len(state)):
			#row j; column i
			sys.stdout.write( str( state[i][j]).rjust(4))
		print 
	print


def find( state, num):
	for i in range(len(state)):
		for j in range(len(state)):
			if( state[i][j] == num):
				return [ i, j]


# given a state and a move, generate the next state
def genState( oState, move):
	state = copy.deepcopy( oState)
	emptySpace = find( state, 0) 
	y = emptySpace[0]
	x = emptySpace[1]

	if( move == 0):
		state[y][x] = state[y-1][x]
		state[y-1][x] = 0

	# move blank space down
	elif( move == 1 ):
		state[y][x] = state[y+1][x]
		state[y+1][x] = 0

	# move blank space left
	elif( move == 2):
		state[y][x] = state[y][x-1]
		state[y][x-1] = 0

	# move blank space right
	else:
		state[y][x] = state[y][x+1]
		state[y][x+1] = 0

	return state



# from available moves return a random move
def randMove( availMoves):
	s = 0
	for i in availMoves:
		s += i 

	r = random.randint( 1, s)
	for i in range(4):
		if( availMoves[i] == 1):
			r -= 1
			if( r == 0):
				return i

# update the available moves
def update( state):
	emptySpace = find( state, 0)
	availMoves = [ 1, 1, 1, 1]
	size = len( state)
	# if top row
	if( emptySpace[0] == 0):
		availMoves[0] = 0
	# if bottom row
	if( emptySpace[0] == size-1):
		availMoves[1] = 0
	# if left side
	if( emptySpace[1] == 0):
		availMoves[2] = 0
	# if right side
	if( emptySpace[1] == size-1):
		availMoves[3] = 0
	return availMoves


# return a n x n board that is shuffled
def init( size):
	board = [[ 0 for x in range( size)] for y in range( size)]
	count = 1

	# initialize board
	while( count < ( size * size)):
		for i in range( size):
			for j in range( size):
				#row j; column i
				board[i][j] = count
				count += 1 
	board[size-1][size-1] = 0

	availMoves = [ 1, 0, 1, 0]
	# shuffle board
	for i in range( 1000):
		move = randMove( availMoves)
		board = genState( board, move)
		availMoves = update( board)

	return board










# bfs search on a state and update the dictionary
def bfs( G, node):
	expand( G, node, 1)





def expand( G, node, depth):
    
    # get next state in pq

    state = node.state
    availMoves = update( state)
    sys.stdout.write('\rStates searched: ' + str(len(G.visited)) )
    sys.stdout.flush()
    # get new state for every legal move
    for i in range(4):
        if( availMoves[i] == 1 ):
            # create state
            nextS = genState( state, i)
            if( getKey( nextS) not in G.visited):
                # havent visited this state, add node to graph

                G.addNode( nextS, node, i, huer(nextS))

            else: #node in graph
                # check if the cost has improved
                old = G.visited[getKey( nextS)]
                oCost = old.depth
                nCost = node.depth + 1
                if( nCost < oCost ):
                    G.updateNode( nextS, node, i)

            if( depth != 0):
            	nextNode = G.visited[getKey( nextS)]
            	expand( G, nextNode, depth - 1)
            	
         


##########################
# Main search
##########################
# given a graph find the terminal state
def search( G):
	sSearch = 0 #states searched





	while (G.pq.qsize() != 0):
		# get next state in pq
		node = G.pq.queue.pop()[1]

		if( tcHuer(node.state) == 0): #terminal state
			return node.backTrack()

		sys.stdout.write('\rStates searched: ' + str(len(G.visited)) )
		sys.stdout.flush()


		bfs(G, node)




def solve( board, path):	
    printBoard( board)
    for move in path:
        print numToWord(move)
        board = genState( board, move)
        printBoard(board)
        time.sleep(1)
    
	