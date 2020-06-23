import math

def read_input(filename):
    with open(filename) as f:
        cities = []
        for line in f.readlines()[1:]:  # Ignore the first line.
            xy = line.split(',')
            cities.append((float(xy[0]), float(xy[1])))
        return cities


def format_solution(solution):
    return 'index\n' + '\n'.join(map(str, solution))


def print_solution(solution):
    print(format_solution(solution))


def distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)


def create_adjacent_matrix(cities):
    N = len(cities)
    dist = [[float('inf')] * N for i in range(N)]
    for i in range(N):
        for j in range(N):
            dist[i][j] = dist[j][i] = distance(cities[i], cities[j])
    
    return dist


def calculate_tour_length(tour_arr, dist_matrix):
    N = len(tour_arr)
    tours_length = list()
  
    for i in range(N):
        total_tour_length = 0
        for j in range(len(tour_arr[i]) - 1):
            source = tour_arr[i][j]
            destination = tour_arr[i][j + 1]
            total_tour_length += dist_matrix[source][destination]
        tours_length.append(total_tour_length)
    
    return tours_length