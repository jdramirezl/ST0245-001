from GraphTimesT4 import Graph
from collections import Counter



def volumes(counter, target, cur):
    if cur > target:
        return False
    if cur == target:
        return True
    
    for key, val in counter.items():
        if val > 0:
            counter[key] -= 1
            if volumes(counter, target, cur + key):
                return True
            counter[key] += 1
    return False



if __name__ == '__main__':
    n = int(input())
    inputs = [(x, Counter([i for i in range(x)]), sum([i for i in range(x)]), 0) for x in range(n)]
    Graph(volumes, inputs, "Volumenes")
    # print(volumes(counter, target, 0))
    