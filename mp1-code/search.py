# search.py
# ---------------
# Licensing Information:  You are free to use or extend this projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to the University of Illinois at Urbana-Champaign
#
# Created by Michael Abir (abir2@illinois.edu) on 08/28/2018

"""
This is the main entry point for MP1. You should only modify code
within this file -- the unrevised staff files will be used for all other
files and classes when code is run, so be careful to not modify anything else.
"""
# Search should return the path and the number of states explored.
# The path should be a list of tuples in the form (row, col) that correspond
# to the positions of the path taken by your search algorithm.
# Number of states explored should be a number.
# maze is a Maze object based on the maze from the file specified by input filename
# searchMethod is the search method specified by --method flag (bfs,dfs,greedy,astar)

from collections import deque
from heapq import heappop, heappush



#Manhattan Distance
def heuristic(curr, nxt):
    return abs(curr[0] - nxt[0]) + abs(curr[1] - nxt[1])

def pt_to_string(pt):
    return str(pt)

def path_to_list(path):
    pt = []
    list = path.split("/")
    for s in list:
        if(s == ""):
            continue
        s = s.replace('(', '')
        s = s.replace(')', '')
        s = s.strip()
        pt.append(tuple(map(int, s.split(','))))
    return pt

def search(maze, searchMethod):
    return {
        "bfs": bfs(maze),
        "dfs": dfs(maze),
        "greedy": greedy(maze),
        "astar": astar(maze),
    }.get(searchMethod, [])


def bfs(maze):
    # TODO: Write your code here
    # return path, num_states_explored
    start = maze.getStart()
    queue = deque([(""+pt_to_string(start)+"/", start)])
    visited = set()
    i = 0
    while queue:
        path, curr = queue.popleft()
        i += 1
        if curr == maze.getObjectives()[0]:
            return path_to_list(path), i
        if curr in visited:
            continue
        visited.add(curr)
        for adj in maze.getNeighbors(curr[0], curr[1]):
            queue.append((path + pt_to_string(adj)+"/", adj))
    return [], i

def dfs(maze):
    # TODO: Write your code here
    # return path, num_states_explored
    start = maze.getStart()
    stack = deque([(""+pt_to_string(start)+"/",start)])
    visited = set()
    i = 0
    while stack:
        path, curr = stack.pop()
        i += 1
        if curr == maze.getObjectives()[0]:
            return path_to_list(path), i
        if curr in visited:
            continue
        visited.add(curr)
        for adj in maze.getNeighbors(curr[0], curr[1]):
            stack.append((path + pt_to_string(adj)+"/", adj))
    return [], i


#Euclidean Distance
def heuristicGreedy(currNode, endNode):
    return (((currNode[0] - endNode[0])**2) + ((currNode[1] - endNode[1])**2))**(1/2)


def greedy(maze):
    # TODO: Write your code here
    # return path, num_states_explored

    start = maze.getStart()
    end = maze.getObjectives()[0]
    hep = []
    heappush(hep, (heuristic(start, end), start, ""+pt_to_string(start)+"/"))
    visited = set()
    i = 0
    while hep:
        cost, currNode, path = heappop(hep)
        i += 1
        if currNode == maze.getObjectives()[0]:
            return path_to_list(path), i
        if currNode in visited:
            continue

        visited.add(currNode)
        for node in maze.getNeighbors(currNode[0], currNode[1]):
            heappush(hep, (heuristic(node, end), node, path + pt_to_string(node)+"/"))

    return [], 0


    # currNode = maze.getStart()
    # path = []
    # visited = set()
    # i = 0
    # endNode = maze.getObjectives()[0]
    # while currNode != endNode:

    #     n_list = maze.getNeighbors(currNode[0], currNode[1])

    #     euclidean_dist = []
    #     for i in n_list:

    #         if i not in visited:
    #             h_sld = ((i[0] - endNode[0])**2 + (i[1]-endNode[1])**2)**(1/2)
    #             euclidean_dist.append(h_sld)

    #     print(euclidean_dist)
    #     min_index = euclidean_dist.index(min(euclidean_dist))

    #     visited.add(currNode)
    #     path.append(currNode)

    #     currNode = n_list[min_index]

    # print(path)

    # return path, len(path)

def astar(maze):
    # TODO: Write your code here
    # return path, num_states_explored
    start = maze.getStart()
    hep = []
    heappush(hep, (0 + heuristic(start, maze.getObjectives()[0]), 0, pt_to_string(start)+"/", start))
    visited = set()
    while hep:
        _, cost, path, curr = heappop(hep)
        if curr == maze.getObjectives()[0]:
            return path_to_list(path), len(visited)
        if curr in visited:
            continue
        visited.add(curr)
        for adj in maze.getNeighbors(curr[0], curr[1]):
            heappush(hep, (cost + heuristic(adj, maze.getObjectives()[0]), cost + 1,
                                path + pt_to_string(adj)+"/", adj))
    return [], 0
