from GraphTimesT4 import Graph


def fibonacci(n):
    if n <= 0:
        return 0
    if n == 1:
        return 1

    return fibonacci(n-2) + fibonacci(n-1)


if __name__ == '__main__':
    n = int(input())
    args = [(x,x) for x in range(n, 35)]
    Graph(fibonacci, args, "Fibonacci")
