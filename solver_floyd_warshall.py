#!/usr/bin/env python3
"""
!! The logic is not fully implemented yet. !!

A solver using Floyd-Warshall Algorithm.
Given V is the number of vertices in the graph, 
Time complexity: O(V^3)
Space complexity: O(V^3)
"""
import sys 
import math 

from common import print_solution, read_input, create_adjacent_matrix
from solver_greedy import format_print_matrix

"""
cities hold a list of tuples holding xy-coordinates of its city
cities = [(x, y), (x, y)]
solve should return a list of city's index 
"""
def solve(cities):
    N = len(cities)
    distance_matrix = create_adjacent_matrix(cities)
    predecessor_matrix = [[0] * N for i in range(N)]
    for i in range(N):
        for j in range(N):
            if i != j:
                predecessor_matrix[i][j] = i
            else: 
                predecessor_matrix[i][j] = None

    """
    Look for shortest path from each city 
    If shortest path exists, update the distance_matrix 
    Also, update the predecessor_matrix, to later find the shortest path from source to destination with min cost
    k = each vertix in the graph considered to be an intermediate vertix 
    """
    for k in range(N):
        for i in range(N):
            for j in range(N):
                if (distance_matrix[i][k] + distance_matrix[k][j] < distance_matrix[i][j]): 
                    distance_matrix[i][j] = distance_matrix[i][k] + distance_matrix[k][j]
                    predecessor_matrix[i][j] = predecessor_matrix[k][j]

    # create result variables to later store output   
    result = ()
    results_list = []
    shortest_path = []

    def print_shortest_path(i, j):
        if i != j:
            print_shortest_path(i, predecessor_matrix[i][j])
        print(f"from {i} -> {j}")
        shortest_path.append(j)

    for i in range(N):
        for j in range(N):
            print_shortest_path(i, j)
            result = (distance_matrix[i][j],) + (shortest_path,)
            results_list.append(result)
            shortest_path.clear()
    
    print(results_list)
    return 0


# Another print function in recursion
def printPath(path, v, u):
	if path[v][u] == v:
		return

	printPath(path, v, path[v][u])
	print(path[v][u], end=' ')


if __name__ == '__main__':
    assert len(sys.argv) > 1
    solution = solve(read_input(sys.argv[1]))
    print_solution(solution)




