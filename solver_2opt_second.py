#!/usr/bin/env python3

import sys 
import math 
import random

from common import print_solution, read_input, distance, create_adjacent_matrix, calculate_tour_length
import solver_nearest_neighbor

def calculate_total_distance(tour_arr, dist_matrix):
    N = len(tour_arr)
    total_tour_length = 0
    for i in range(N - 1):
        source = tour_arr[i]
        destination = tour_arr[i + 1]
        total_tour_length += dist_matrix[source][destination]
    
    return total_tour_length


def calculate_2opt_exchange_cost(visit_order, i, j, distance_matrix):
    """Calculate the difference of cost by applying given 2-opt exchange"""
    n_cities = len(visit_order)
    a, b = visit_order[i], visit_order[(i + 1) % n_cities]
    c, d = visit_order[j], visit_order[(j + 1) % n_cities]

    cost_before = distance_matrix[a][b] + distance_matrix[c][d]
    cost_after = distance_matrix[a][c] + distance_matrix[b][d]
    return cost_after - cost_before


def apply_2opt_exchange(visit_order, i, j):
    """Apply 2-opt exhanging on visit order"""

    tmp = visit_order[i + 1: j + 1]
    tmp.reverse()
    visit_order[i + 1: j + 1] = tmp

    return visit_order


def improve_with_2opt(visit_order, distance_matrix):
    """Check all 2-opt neighbors and improve the visit order"""
    n_cities = len(visit_order)
    cost_diff_best = 0.0
    i_best, j_best = None, None

    for i in range(0, n_cities - 2):
        for j in range(i + 2, n_cities):
            if i == 0 and j == n_cities - 1:
                continue

            cost_diff = calculate_2opt_exchange_cost(
                visit_order, i, j, distance_matrix)

            if cost_diff < cost_diff_best:
                cost_diff_best = cost_diff
                i_best, j_best = i, j

    if cost_diff_best < 0.0:
        visit_order_new = apply_2opt_exchange(visit_order, i_best, j_best)
        return visit_order_new
    else:
        return None


def local_search(distance_matrix, start_city):
    """Main procedure of local search"""
    visit_order = solver_nearest_neighbor.nearest_neighbor(distance_matrix, start_city)
    cost_total = calculate_total_distance(visit_order, distance_matrix)

    while True:
        improved = improve_with_2opt(visit_order, distance_matrix)
        if not improved:
            break

        visit_order = improved

    return visit_order


def solve(cities):
    N = len(cities)
    start_cities = [i for i in range(N)]

    if N >= 512:
        start_cities = [random.randint(0, N-1)]

    dist_matrix = create_adjacent_matrix(cities)
    tours = []

    for i in start_cities:
        tours.append(local_search(dist_matrix, i))
    
    tour_length_arr = calculate_tour_length(tours, dist_matrix)
    tour_index = tour_length_arr.index(min(tour_length_arr))
    shortest_tour = tours[tour_index]
    return shortest_tour


    
if __name__ == '__main__':
    assert len(sys.argv) > 1
    solution = solve(read_input(sys.argv[1]))
    print_solution(solution)