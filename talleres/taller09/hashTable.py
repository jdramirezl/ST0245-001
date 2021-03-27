class HashTable:
    def __init__(self):
        self.table = [None] * 50

    def set(self, name, num):
        total = 0
        for i in name:
            total += ord(i)
        self.table[total%20] = num

    def get(self, name):
        total = 0
        for i in name:
            total += ord(i)
        return self.table[total%20]