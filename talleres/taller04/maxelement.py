from GraphTimesT4 import Graph
import random as rand

def maximum_number(lista, maxInt, index):
    if index >= len(lista):
        return maxInt
    print(max(lista[index], maxInt))
    return maximum_number(lista, max(lista[index], maxInt), index + 1)


if __name__ == '__main__':
    inputs = [(x, [rand.randint(1, 100) for _ in range(x)], sum(
        [i for i in range(x)]), 0) for x in range(1, 1000, 20)]
    Graph(maximum_number, inputs, "Max Number")
    # print(volumes(counter, target, 0))
