from collections import defaultdict
from sortedcontainers import SortedList
import math

INF = math.inf


def dfs(graph, start, max_time, picked, visited, target, p_multiplier, shortest_times):
    visited.append(start)
    if visited[-1] == target:
        return visited
    elif len(visited) >= 5 and visited[-1] != target:
        return []

    path = []
    for node in graph[start]:
        next = node[1]
        time_next = node[0]

        if next in visited or next in picked or (time_next > max_time):
            continue

        tmp = visited.copy()
        route = dfs(graph, next, (max_time - time_next), picked,
                    tmp, target, p_multiplier, shortest_times)
        path = route if len(route) > len(path) else path

    return path


def main(graph, vertices, shortest_times, p_multiplier):
    # Initialize variables
    visited = set()
    cars = 0

    # Organize car list
    nodes = list(shortest_times.items())
    nodes.sort(key=lambda x: x[1], reverse=True)

    # Iterate through nodes
    for node, val in nodes:
        print()
        print("New round")

        if node in visited:
            continue

        max_time = shortest_times[node]
        print("max time", max_time, "for node", node)

        # Perform DFS
        path = dfs(graph, node, max_time, visited, list(),
                   1, p_multiplier, shortest_times)

        # Add picked cars to visited
        for car in path:
            visited.add(car)
        #print("Path", path)
        #print("visited", visited)
        cars += 1

    print("Minimum num of cars:", cars)


def process_data():

    directory = './datasets/dataset-ejemplo-U=11-p=1.3.txt'

    with open(directory, 'r', encoding='utf-8') as f:
    #f = open(directory)
        _ignore, p = f.readline().split(' ')
        p = float(p)

        for i in range(3):
            f.readline()

        nodes = 0
        while True:
            line = f.readline()
            nodes = line.split(' ')[0] if line.split(' ')[0] != '\n' else nodes
            if line.split(' ')[0] == '\n':
                break

        for i in range(2):
            f.readline()

        graph = defaultdict(list)
        shortest_times = defaultdict(int)
        while True:
            line = f.readline()
            if line == '':
                break

            start, end, weight = map(int, line.split(' '))
            if start == 1:
                continue

            if end == 1:
                shortest_times[start] = weight * p

            graph[start].append((weight, end))

        # print(graph)
        main(graph, nodes, shortest_times, p)


if __name__ == "__main__":
    process_data()
