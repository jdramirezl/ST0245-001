import os
from PIL import Image as i
from numpy import genfromtxt

class Image:
    def __init__(self, directory, image_output):
        self.directory = directory
        self.image_output = image_output
        self.process()
    
    def save_image(self, file):
        g = open(self.directory+'/'+file,'r')
        temp = genfromtxt(g, delimiter = ',')
        im = i.fromarray(temp).convert('L')
        # im.show()
        im.save(self.image_output+'/'+file[:-4] + '.png')
        g.close()
    
    def process(self):
        # Read Files
        files = [file for file in os.listdir(self.directory) if file.endswith(("csv",))]
        
        # Process
        for file in files:
            self.save_image(file)


