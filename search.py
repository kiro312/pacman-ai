# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()

def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return [s, s, w, s, w, w, s, w]

def InQueue(item, queue):
    for queue_item in queue.list:
        if queue_item[0] == item:
            return True
    return False

# def generalGraphSearch(problem, data_structure):
#     print(data_structure)
#     from util import Stack
#     node_point = problem.getStartState()  # initialize the first node
#     # print('node_point is : ' , node_point)
#     if problem.isGoalState(node_point):
#         return []
#     node_path = []
#     data_structure.push([node_point, node_path])  # push to the structure the first node with an empty path
#     explored_list = []

#     while not data_structure.isEmpty():  # as long as the structure is not empty
#         node, path = data_structure.pop()  # we pop a nude and a path
#         # print("node is :", node)
#         # print("path is :", path)
#         if problem.isGoalState(node):  # check the node
#             return path  # return the path if needed
#         explored_list.append(node)  # else we mark it as visited
#         successor = problem.getSuccessors(node)  # then we add all of is successor to the stack
#         if successor:  # if there is a successor
#             print('suc is: ', successor)
#             for successor_node in successor:  # loop on all of the successors
#                 if successor_node[0] not in explored_list:  # consider only the unvisited nodes
#                     if isinstance(data_structure, Stack) or not InQueue(successor_node[0], data_structure):  # if stack we can just scan
#                         data_structure.push((successor_node[0], path + [successor_node[1]]))  # add to the stack
#     return []  # if the func reaches here it means no path was found therefore we return an empty list

def depthFirstSearch(problem):
    node_point = problem.getStartState()
    if problem.isGoalState(node_point):
        return []

    node_path = []
    frontier = util.Stack()
    frontier.push([node_point, node_path])
    visited = []

    while not frontier.isEmpty():   
        node, path = frontier.pop()

        if problem.isGoalState(node):
          return path

        visited.append(node)
        successors = problem.getSuccessors(node)

        for successor in successors:
            if successor[0] not in visited:
                frontier.push((successor[0], path + [successor[1]]))
    return []

def breadthFirstSearch(problem):
    node_point = problem.getStartState()
    if problem.isGoalState(node_point):
        return []
    node_path = []
    frontier = util.Queue()
    frontier.push([node_point, node_path])
    
    visited = []
    while not frontier.isEmpty():        
        node, path = frontier.pop()

        if problem.isGoalState(node):
          return path

        visited.append(node)
        successors = problem.getSuccessors(node)

        for child in successors:
            if child[0] not in visited:
                frontier.push((child[0], path + [child[1]]))
    return []

def inPriorityQueue(item, queue):
    for queue_item in queue.heap:
        if queue_item[2][0] == item:
            return True
    return False

def uniformCostSearch(problem):
    start = problem.getStartState()
    if problem.isGoalState(start):
        return []

    frontier = util.PriorityQueue()
    node_path = []
    frontier.push((start, node_path), 0)
    visited = []

    while not frontier.isEmpty():
        node, path = frontier.pop()

        if problem.isGoalState(node):
            return path

        if node not in visited:

            visited.append(node)
            successors = problem.getSuccessors(node)

            if successors:
                for successor in successors:
                    newpath = path + [successor[1]]
                    frontier.push( (successor[0],newpath), problem.getCostOfActions(newpath) )
    return []

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
        node = problem.getStartState()
        visited=[]
        frontier=util.PriorityQueue()
        path = []

        frontier.push( (node, path), nullHeuristic(node, problem))

        newcost=0

        while not frontier.isEmpty():
            node, path = frontier.pop()

            if problem.isGoalState(node):
                return path

            if node not in visited:
                visited.append(node)

                successors = problem.getSuccessors(node)

                for successor in successors:
                    newpath = path + [successor[1]]
                    newcost = problem.getCostOfActions(newpath) + heuristic(successor[0], problem)
                    frontier.push( (successor[0], newpath), newcost)
        return [] 


def greedyBestFirstSearch(problem, heuristic=nullHeuristic):  
        start=problem.getStartState()

        visited=[]

        frontier = util.PriorityQueue()
        path = []

        frontier.push((start,path), nullHeuristic(start,problem))
        newcost = 0
        while not frontier.isEmpty():
            node,path = frontier.pop()
            if problem.isGoalState(node):
                return path
            if node not in visited:
                visited.append(node)
                successors = problem.getSuccessors(node)
                if successors:
                    for successor in successors:
                        newpath = path + [successor[1]]
                        newcost = heuristic(successor[0], problem)
                        frontier.push( (successor[0], newpath) , newcost)
        return [] 

# Commands
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
gbfs = greedyBestFirstSearch