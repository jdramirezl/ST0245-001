import csv
import RunLength as rl
import os
from SeamCarving import SC
from ImageScaling import Scaling


class File:
    def __init__(self, filename, compression, destination=None):
        self.filename = filename
        self.destination = destination
        self.data = []
        self.read_file() 
        self.to_int() if compression else 0
        self.proccess(compression)

    def proccess(self, compress):
        if compress:
            result = "compressed"
            self.scale()
            self.seam_carving()
            self.run_length()
        else:
            result = "decompressed"
            self.reverse_run_length()
            # self.descale()
            self.filename = self.filename[12:]
        
        dir = os.getcwd()
        os.chdir(self.destination)
        file_name = self.filename.split("/")[-1]
        
        with open(f"{result}-{file_name}", 'w', newline="") as csv_file:
            writer = csv.writer(csv_file, delimiter=',')
            for row in self.data:
                writer.writerow(row)
        os.chdir(dir)

    def read_file(self):
        with open(self.filename, 'r') as csv_file:
            csv_reader = csv.reader(csv_file)
            for row in csv_reader:
                self.data.append(row)

    def to_int(self):
        #print(self.filename)
        self.data = [[int(value) for value in row] for row in self.data]

    def seam_carving(self):
        self.data = SC(self.data).return_list()

    def run_length(self):
        self.data = rl.RunLength.compress(self.data)

    def reverse_run_length(self):
        self.data = rl.RunLength.decompress(self.data)

    def scale(self):
        self.data = Scaling.scale(self.data)

    def descale(self):
        self.data = Scaling.descale(self.data)

    def __str__(self):
        return self.filename
