import sys


from graph import Graph
from agent import *


def numToWord( n):
	if(n == 0): 
		print 'up'
	elif(n == 1): 
		print 'down'
	elif(n == 2):
		print 'left'
	else:
		print 'right'




##########################
#   MAIN
##########################

size = 3
fName = 'stats' + str(size)
file = open( fName, 'a+')



for i in range( 100):
    board = init(size)
    #printBoard(board)
    G = Graph( board)

    path = search(G)
    
    states = str(len(G.visited))
    file.write( states + '\n')
    sys.stdout.write('\rGame ' + str(i) + ': ' + states + '                ')
    sys.stdout.flush()
    print

file.close()
'''


games = 0
states = 0
for i in range( 5):
	moves = 0
	B = Board( 3)
	B.shuffle()

	G = Graph( B)
	#print 'initial board'
	#B.printBoard()
	path =  search( G )
 	state = len(path)
	states += state 
	games += 1
	
	sys.stdout.write('\rGames played: ' +  str(games) +'  Last games states: ' + str(state))
	sys.stdout.flush()

avg = states / games
file.write( str(avg))
print
'''
