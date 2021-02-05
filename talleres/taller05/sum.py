from GraphTimesT5 import Graph
import time
# import threading
import multiprocessing


def suma2(lista):
    print(sum(lista))
    return sum(lista)


def suma_ciclos(lista):
    total = 0
    time.sleep(0.0001 * len(lista))
    for i in range(len(lista)):
        total += lista[i]
    return total


def suma_recursiva(lista, index=0, total=0):
    time.sleep(0.0000001)
    if index == len(lista):
        return total
    return suma_recursiva(lista, index+1, total + lista[index])

def func(*args):
    Graph(*args)


if __name__ == '__main__':
    inputs = [(x, [i for i in range(1, x+1)]) for x in range(1, 1001, 10)]
    
    t1 = multiprocessing.Process(target=func, args=(suma_ciclos, inputs, "Cycle Sum"))
    
    inputs = [(x, [i for i in range(1, x+1)]) for x in range(1, 1001, 50)]
    t2 = multiprocessing.Process(target=func, args=(suma_recursiva, inputs, "Recursive Sum"))
    

    t1.start() 
    t2.start() 
    
