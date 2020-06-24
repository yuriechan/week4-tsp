#!/usr/bin/env python3

import sys
import math 

from common import print_solution, read_input, distance, create_adjacent_matrix

def format_print_matrix(matrix):
    print('\n'.join(['           '.join(['{:4}'.format(item) for item in row]) 
      for row in matrix]))

def sort_by_x_coordinate(cities):
    return [b[0] for b in sorted(enumerate(cities), key=lambda i:i[1][0])]
    

def solve(cities):
    x_ascending_city = sort_by_x_coordinate(cities)
    return x_ascending_city

    # The below implementation was not used since the graph failed to traverse by its level without adding constraints such as ordering by x-coordinates.  
    """
    N = len(cities)
    dist_matrix = create_adjacent_matrix(cities)
    print(dist_matrix)

    start_city = 0
    visited_cities = [False for i in range(N)]
    print(f"visited_cities: {visited_cities}")
    queue = [start_city]
    print(f"queue: {queue}")
    visited_cities[start_city] = True
    visited_cities_index = None
    path = list()

    while queue:
        visited_cities_index = queue[0]
        print(f"visited_cities_index: {visited_cities_index}")
        path.append(visited_cities_index)
        print(f"path: {path}")
        queue.pop(0)
        print(visited_cities_index)
        for i in range(N):
            print(f"visited_cities: {visited_cities}")
            print(f"i:{i}")
            print(f"dist_matrix[visited_cities_index][i]: {dist_matrix[visited_cities_index][i]}")
            print(f"visited_cities[i]: {visited_cities[i]}")
            if dist_matrix[visited_cities_index][i] is not 0.0 and not(visited_cities[i]):
                queue.append(i)
                visited_cities[i] = True

    print(path)
    """


if __name__ == '__main__':
    assert len(sys.argv) > 1
    solution = solve(read_input(sys.argv[1]))
    print_solution(solution)