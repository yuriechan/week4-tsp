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


def calculate_tour_length(tour_arr, dist_matrix):
    # number of tours to calculate its length
    N = len(tour_arr)
    tours_length = list()

    for i in range(N):
        total_tour_length = 0
        for j in range(len(tour_arr[i]) - 1):
            source = tour_arr[i][j]
            destination = tour_arr[i][j + 1]
            print(f"source:{source}")
            print(f"destination:{destination}")
            print(f"dist_matrix[source][destination]: {dist_matrix[source][destination]}")
            total_tour_length += dist_matrix[source][destination]
        tours_length.append(total_tour_length)
    
    return tours_length

def solve(cities):
    N = len(cities)
    dist_matrix = create_adjacent_matrix(cities)
    tours = []
    
    for i in range(N):
        tours.append(nearest_neighbor(dist_matrix, i))

    tour_length_arr = calculate_tour_length(tours, dist_matrix)
    tour_index = tour_length_arr.index(min(tour_length_arr))
    #print(tour_length_arr)
    #print(min(tour_length_arr))
    #print(tour_length_arr.index(min(tour_length_arr)))
    shortest_tour = tours[tour_index]
    return shortest_tour


if __name__ == '__main__':
    assert len(sys.argv) > 1
    solution = solve(read_input(sys.argv[1]))
    print_solution(solution)
