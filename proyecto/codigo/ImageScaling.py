import numpy as np
import numpy
from collections import deque


class Scaling:

    @staticmethod
    def scale(data):
        im = np.array(data)

        factor = 2
        x = im.shape[0] // factor
        y = im.shape[1] // factor
        output = []

        for i in range(x):
            row = []
            for j in range(y):
                row.append(im[i * factor][j * factor])
            output.append(row)

        return output

    @staticmethod
    def descale(data):
        im = numpy.array(data)

        factor = 2
        m = im.shape[0]
        n = im.shape[1]
        m_new = m * factor
        n_new = n * factor

        output = [[0 for _ in range(n_new)] for _ in range(m_new)]

        for i in range(m):
            for j in range(n):
                output[i * factor][j * factor] = im[i][j]
                queue = deque()
                queue.append((i * factor, j * factor))
                iterations = factor // 2
                visited = set()
                visited.add((i * factor, j * factor))
                while queue and iterations:
                    temp = deque()
                    while queue:
                        a, b = queue.popleft()
                        for x, y in ((0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)):
                            if 0 <= a + x < m * factor and 0 <= b + y < n * factor and not (a + x, b + y) in visited:
                                temp.append((a + x, b + y))
                                visited.add((a + x, b + y))
                                output[a + x][b + y] = output[i * factor][j * factor]
                    iterations -= 1
        return output
