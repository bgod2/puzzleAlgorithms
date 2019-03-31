import random
import sys
import copy

##########################
# puzzle board
##########################

class Board:
	"""
	Sliding tile puzzle board
	"""
	#create nxn board
	def __init__( self, size):
		
		self.size = size
		self.emptySpace = [size-1, size-1]
						#   U  D  L  R
		self.availMoves = [ 1, 0, 1, 0]
	
		#initialize board
		self.board = [[ 0 for x in range( self.size)] for y in range( self.size)]
		count = 1

		while( count < ( self.size * self.size)):
			for i in range( self.size):
				for j in range( self.size):
					#row j; column i
					self.board[i][j] = count
					count += 1 
		self.board[size-1][size-1] = 0

	# shuffle the board for the start
	def shuffle( self):
		for i in range( 1000):
			move = self.randMove()
			self.swap( move)


	# return the board state
	def getState(self):
		return self.board


	# set the board state
	def setState(self, board):
		self.board = board
		self.update()


	# return a new board state by making a legal move
	def genState( self, move):
		# clone board state, make move, return state
		b = copy.deepcopy( self)
		b.swap(move)
		return b


	# move the blank space, and the corresponding tile
	def swap( self, move):
		y = self.emptySpace[0]
		x = self.emptySpace[1]

		# move blank space up
		if( move == 0):
			self.board[y][x] = self.board[y-1][x]
			self.board[y-1][x] = 0
			self.emptySpace = [ y-1, x]

		# move blank space down
		elif( move == 1 ):
			self.board[y][x] = self.board[y+1][x]
			self.board[y+1][x] = 0
			self.emptySpace = [ y+1, x]

		# move blank space left
		elif( move == 2):
			self.board[y][x] = self.board[y][x-1]
			self.board[y][x-1] = 0
			self.emptySpace = [ y, x-1]

		# move blank space right
		else:
			self.board[y][x] = self.board[y][x+1]
			self.board[y][x+1] = 0
			self.emptySpace = [y, x+1]
		self.update()



	# select a random move from the available moves 
	def randMove( self):
		s = 0
		for i in self.availMoves:
			s += i 

		r = random.randint( 1, s)
		for i in range(4):
			if( self.availMoves[i] == 1):
				r -= 1
				if( r == 0):
					return i


	# update the possible moves 
	def update( self):
		self.emptySpace = self.find(0)
		self.availMoves = [ 1, 1, 1, 1]
		# if top row
		if( self.emptySpace[0] == 0):
			self.availMoves[0] = 0
		# if bottom row
		if( self.emptySpace[0] == self.size-1):
			self.availMoves[1] = 0
		# if left side
		if( self.emptySpace[1] == 0):
			self.availMoves[2] = 0
		# if right side
		if( self.emptySpace[1] == self.size-1):
			self.availMoves[3] = 0


	#print the current board state
	def printBoard( self):
		print
		for i in range( self.size):
			for j in range( self.size):
				#row j; column i
				sys.stdout.write( str( self.board[i][j]).rjust(4))
			print 
		print
		
	# find a number in the board
	def find( self, num):
		for i in range( self.size):
			for j in range( self.size):
				if( self.board[i][j] == num):
					return [ i, j]


	def huer( self):
		dist = 0
		num = 1
		for i  in range( self.size):
			for j in range( self.size):
				actual = self.find( num)
				dist += abs( actual[0] - i)
				dist += abs( actual[1] - j)

				num += 1
				if(num == self.size * self.size): 
					return dist


	def getKey( self):
		key = ''
		for i in range(self.size):
			for j in range(self.size):
				key += str(self.board[i][j]) + ','
		return key