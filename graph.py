# initial code taken from
# http://www.bogotobogo.com/python/python_graph_data_structures.php
# changes were made to suit the needs of my code
import Queue
from agent import huer, printBoard, numToWord
import time



# return the dictionary key for the state



def getKey( state):
    key = []
    for i in state:
        for j in i:
            key.append(j)
    return str( key).strip('[]')

class Node:
    """docstring for Node"""
    def __init__( self, state, parent, move, depth):
        self.depth = depth
        self.state = state 
        self.move = move
        self.parent = parent


    #once the goal is found, create the path recursively
    def backTrack( self):
        if( self.parent == None):
            return []
        else:
            path = self.parent.backTrack()
            path.append(self.move)
            
            return path


class Graph:
    """docstring for Graph"""
    def __init__( self, initState ):
        self.visited = {}
        self.pq = Queue.PriorityQueue()

        initNode = Node(initState, None, None, 0)
        self.visited[ getKey( initState)] = initNode
        self.pq.put(( -huer(initState), initNode)) 


    def addNode( self, state, parent, move, huer):
        #create node
        node = Node( state, parent, move, parent.depth + 1)
        

        self.pq.put(( -huer, node))
        self.visited[ getKey( state)] = node

    def printLen( self):
        print self.pq.qsize()

    def updateNode( self, state, parent, move):
        node = self.visited[ getKey(state)]
        node.parent = parent
        node.move = move
        node.depth = parent.depth