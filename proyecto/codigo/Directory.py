import os
import File as f


class Directory:
    def __init__(self, directory):
        self.directory = directory
        self.get_filenames()
        self.load_files()
        

    def get_filenames(self):
        self.filenames = [os.path.join(self.directory, file) for file in os.listdir(self.directory) if file.endswith(("csv",))]

    def load_files(self):
        self.files = [f.File(filename) for filename in self.filenames]
