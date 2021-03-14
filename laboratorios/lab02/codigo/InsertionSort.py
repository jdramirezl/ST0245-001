from random import randrange
from Graph import Graph
import time

def insertionSort(arr):
    for i in range(1, len(arr)):
        
        key = arr[i]
        j = i-1
        while j >= 0 and key < arr[j] :
                time.sleep(0.001)
                arr[j + 1] = arr[j]
                j -= 1
        arr[j + 1] = key
        

def main():
    args = [[randrange(1, 1000) for x in range(i*10)] for i in range(1, 21)]
    for arg in args:
        print(len(arg))
    Graph(insertionSort, args, "insertionSort")

main()