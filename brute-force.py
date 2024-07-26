import itertools
import timeit

def read_matrix(file):
    with open(file, 'r') as f:
        return [list(line.strip()) for line in f.readlines()[1:]]

def find_points(matrix):
    return {char: (i, j) for i, row in enumerate(matrix) for j, char in enumerate(row) if char != '0'}

taxi_geometry = lambda p1, p2: abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

def route_cost(route, points):
    return sum(taxi_geometry(points[route[i]], points[route[i + 1]]) for i in range(len(route) - 1))

def find_best_route(points):
    deliveries = [point for point in points if point != 'R']
    return ''.join(min(itertools.permutations(deliveries), key=lambda perm: route_cost(['R'] + list(perm) + ['R'], points)))

def main():
    matrix = read_matrix('input.txt')
    points = find_points(matrix)
    start_time = timeit.default_timer()
    best_route = find_best_route(points)
    print("Best route:", best_route)
    print("Execution time: {:.4f} seconds".format(timeit.default_timer() - start_time))

if __name__ == '__main__':
    main()
