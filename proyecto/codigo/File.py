import csv
import RunLength as rl
import os
from SeamCarving import SC


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
            self.seam_carving()
            self.run_length()
        else:
            result = "decompressed"
            self.reverse_run_length()
            self.filename = self.filename[12:]
        
        dir = os.getcwd()
        os.chdir(self.destination)
        file_name = self.filename.split("/")[-1]
        
        with open(f"{result}-{file_name}", 'w', newline="") as csvfile: 
            writer = csv.writer(csvfile, delimiter=',')
            for row in self.data:
                writer.writerow(row)
        os.chdir(dir)

    def read_file(self):
        with open(self.filename, 'r') as csvfile:
            csvreader = csv.reader(csvfile)
            for row in csvreader:
                self.data.append(row)

    def to_int(self):
        print(self.filename)
        self.data = [[int(value) for value in row] for row in self.data]

    def seam_carving(self):
        self.data = SC(self.data).return_list()

    def run_length(self):
        self.data = rl.RunLength.compress(self.data)

    def reverse_run_length(self):
        self.data = rl.RunLength.decompress(self.data)

    def __str__(self):
        return self.filename
    
    
    
    
'''
    def compress(self):
        #self.seam_carving()
        self.run_length()
        dir = os.getcwd()
        os.chdir(self.destination)
        file_name = self.filename.split("/")[-1]
        file_name = file_name.split("\\")[-1]
        with open(f"compressed-{file_name}", 'w', newline="") as csvfile: 
            writer = csv.writer(csvfile, delimiter=',')
            for row in self.data:
                writer.writerow(row)
        os.chdir(dir)


    def decompress(self):
        self.reverse_run_length()
        dir = os.getcwd()
        os.chdir(self.destination)
        file_name = self.filename.split("/")[-1]
        file_name = file_name.split("\\")[-1]
        with open(f"decompressed-{file_name}", 'w', newline="") as csvfile: 
            writer = csv.writer(csvfile, delimiter=',')
            for row in self.data:
                writer.writerow(row)
        os.chdir(dir)
'''