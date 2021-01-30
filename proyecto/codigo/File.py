import csv
import os


class File:
    def __init__(self, filename):
        self.filename = filename
        self.data = []
        self.read_file()
        self.to_int()
        # print(self.data)

    def write_file(self, file):
        with open(self.filename, 'r') as csvfile:
            pass

    def read_file(self):
        with open(self.filename, 'r') as csvfile:
            csvreader = csv.reader(csvfile)
            for row in csvreader:
                self.data.append(row)

    def to_int(self):
        self.data = [[float(value) for value in row] for row in self.data]

    def __str__(self):
        return self.filename
