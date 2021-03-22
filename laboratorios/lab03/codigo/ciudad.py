class Node:
    def __init__(self, id, x, y, name=None):
        self.id = int(id)
        self.x = float(x)
        self.y = float(y)
        self.locations = name


def main():
    medellin = []
    with open("medellin_colombia-grande.txt", "r") as file:
        i = -1
        while f:= file.readline():
            i += 1
            if i == 0: continue
            args = f.split()
            nums ,locations = args[0:3], args[3:]
            if not nums: break
            medellin.append(Node(*nums, locations))

    return medellin

if __name__ == '__main__':
    print(main())


