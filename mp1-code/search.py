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

def greedy(maze):
    # TODO: Write your code here
    # return path, num_states_explored
    return [], 0

def astar(maze):
    # TODO: Write your code here
    # return path, num_states_explored
    start = maze.getStart()
    hep = []
    heappush(hep, (0 + heuristic(start, maze.getObjectives()[0]), 0, "", start))
    visited = set()
    while hep:
        _, cost, path, curr = heappop(hep)
        if curr == maze.getObjectives()[0]:
            return path
        if curr in visited:
            continue
        visited.add(curr)
        for adj in maze.getNeighbors(curr[0], curr[1]):
            heappush(hep, (cost + heuristic(adj, maze.getObjectives()[0]), cost + 1,
                                path + pt_to_string(adj)+"/", adj))
    return [], 0
