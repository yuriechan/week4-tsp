#!/usr/bin/env python3

import sys
import math

from common import print_solution, read_input


def distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def format_print_matrix(matrix):
    print('\n'.join(['           '.join(['{:4}'.format(item) for item in row]) 
      for row in matrix]))

def create_adjacent_matrix(cities):
    N = len(cities)
    dist = [[0] * N for i in range(N)]
    for i in range(N):
        for j in range(N):
            dist[i][j] = dist[j][i] = distance(cities[i], cities[j])
    
    return dist

def nearest_neighbor(dist_matrix, start_city=0):
    # number of vertex in the graph (number of city)
    N = len(dist_matrix)

    unvisited_cities = set(range(0, N))
    unvisited_cities.remove(start_city)
    tour = [start_city]
    current_city = start_city

    def distance_from_current_city(to):
        return dist_matrix[current_city][to]

    while unvisited_cities:
        # get the unvisited city closest to the city most recently visited 
        next_city = min(unvisited_cities, key=distance_from_current_city)
        unvisited_cities.remove(next_city)
        tour.append(next_city)
        current_city = next_city
    return tour

def solve(cities):
    N = len(cities)
    dist_matrix = create_adjacent_matrix(cities)
    tours = []
    
    for i in range(N):
        tours.append(nearest_neighbor(dist_matrix, i))

    print(tours)
    return None


if __name__ == '__main__':
    assert len(sys.argv) > 1
    solution = solve(read_input(sys.argv[1]))
    print_solution(solution)
