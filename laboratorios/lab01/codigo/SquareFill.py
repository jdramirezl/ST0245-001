from random import randrange

COLORS = [
    '\33[31m \33[0m',
    '\33[32m \33[0m',
    '\33[33m \33[0m',
    '\33[34m \33[0m',
    '\33[35m \33[0m'
]


def print_matrix(matrix):
    for i in matrix:
        for j in i:
            print(j, end=' ')
        
        print()


def get_color(matrix, i):
    num = randrange(0, 4)
    while i > 0 and matrix[num] == matrix[0][i-1]:
        num = randrange(0,4)
    first = COLORS[num]
    while COLORS[num] != first or (i > 0 and matrix[num] == matrix[1][i - 1]):
        num = randrange(0,4)
    second = COLORS[num]
    return first, second


def color(matrix, i, vertical, func):
    color_one, color_two = get_color(matrix, i)
    if vertical:
        matrix[0][i] = color_one
        matrix[1][i] = color_one
        val = func(matrix, i + 1)
        matrix[0][i] = " "
        matrix[1][i] = " "
    else:
        matrix[0][i] = color_one
        matrix[0][i+1] = color_one
        matrix[1][i] = color_two
        matrix[1][i+1] = color_two
        val = func(matrix, i + 1)
        matrix[0][i] = " "
        matrix[0][i+1] = " "
        matrix[1][i] = " "
        matrix[1][i+1] = " "
    return val


def fill(matrix, i):
    if i >= len(square) - 1:
        
        print_matrix(square)
        return 1

    vertical = color(matrix, i, True, fill)
    horizontal = 0
    if i + 1 < len(square):
        horizontal = color(matrix, i, False, fill)
    return vertical + horizontal


if __name__ == "__main__":
    n = int(input())
    square = [[" " for _ in range(n)]  * 2]
    print("Numero de maneras: " +  str(fill(square, 0)))

# Implementen  un  algoritmo  recursivo
# para  encontrar  de  cuántas  formas  se
# puede llenar un rectángulo de 2xn cm2 con rectángulos de 1x2 cm².

