from random import randrange

COLORS = [
    '\33[41m \033[0m',
    '\33[42m \033[0m',
    '\33[43m \033[0m',
    '\33[44m \033[0m',
    '\33[45m \033[0m',
    '\33[46m \033[0m',
    '\33[47m \033[0m',
    # '\33[48m \033[0m',
    # '\33[49m \033[0m',
    # '\33[50m \033[0m'
]


def print_matrix(matrix):
    for i in matrix:
        for j in i:
            print(j, end='')

        print()


def get_color(matrix, i):
    num = randrange(0, 6)
    while i > 0 and (COLORS[num] == matrix[0][i-1] or COLORS[num] == matrix[1][i-1]):
        num = randrange(0, 6)
    first = COLORS[num]

    while COLORS[num] == first or (i > 0 and COLORS[num] == matrix[1][i - 1]):
        num = randrange(0, 6)
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
        val = func(matrix, i + 2)
        matrix[0][i] = " "
        matrix[0][i+1] = " "
        matrix[1][i] = " "
        matrix[1][i+1] = " "
    return val


def fill(matrix, i):
    if i >= len(matrix[0]):
        print("Diff")
        print_matrix(matrix)
        return 1

    vertical = color(matrix, i, True, fill)
    horizontal = 0
    if i + 1 < len(matrix[0]):
        horizontal = color(matrix, i, False, fill)
    return vertical + horizontal


if __name__ == "__main__":
    n = int(input())
    square = []
    temp = []
    temp2 = []
    for j in range(n):
        temp.append("0")
    for j in range(n):
        temp2.append("0")

    square.append(temp)
    square.append(temp2)

    print("Numero de maneras: " + str(fill(square, 0)))

# Implementen  un  algoritmo  recursivo
# para  encontrar  de  cuántas  formas  se
# puede llenar un rectángulo de 2xn cm2 con rectángulos de 1x2 cm².
