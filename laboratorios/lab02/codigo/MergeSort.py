from random import randrange
from Graph import Graph
import time

def mergeSort(arr):
    if len(arr) > 1:
        mid = len(arr)//2

        L = arr[:mid]
        R = arr[mid:]

        mergeSort(L)
        mergeSort(R)

        i = j = k = 0

        while i < len(L) and j < len(R):
            time.sleep(0.001)
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
            

def main():
    args = [[randrange(1, 1000) for x in range(i*10)] for i in range(1, 21)]
    for arg in args:
        print(len(arg))
    Graph(mergeSort, args, "Merge Sort")

main()