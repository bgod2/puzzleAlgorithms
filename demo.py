import sys
import copy

from graph import Graph
from agent import *



##########################
#   MAIN
##########################

size = 3

fboard = open('board', 'r+')


board = init(size)
board1 = copy.deepcopy(board)
print 'Initial board'
printBoard(board)
G = Graph( board)
path = search(G)
solve( board1, path)



