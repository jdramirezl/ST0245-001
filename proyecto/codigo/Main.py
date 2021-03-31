import os
from File import File
from Images import Image

def process(directory, output, compression):
    # Read Files
    files = [f"{directory}/{file}" for file in os.listdir(directory) if file.endswith(("csv",))]
    
    # Process
    for path in files:
        f = File(path, compression=compression, destination=output)
        del f

def process_images(directory, compressed_output, decompressed_output):
    # Compress
    process(directory, compressed_output, True)
    
    # Decompress
    process(compressed_output, decompressed_output, False)

def main():
    # Process Sick
    directory = "datasets/archivosCSV/ganado enfermo CSVs"
    compressed_output = "Output/Compressed/Sick"
    decompressed_output = "Output/Decompressed/sick"
    
    process_images(directory, compressed_output, decompressed_output)
    
    image_output = "Images/Sick"
    Image(decompressed_output, image_output)
    
    '''
    # Process Healthy
    directory = "datasets/archivosCSV/ganado sano CSVs"
    compressed_output = "Output/Compressed/Healthy"
    decompressed_output = "Output/Decompressed/Healthy"
    image_output = "Images/Healthy"
    process_images(directory, compressed_output, decompressed_output)
    '''
    


if __name__ == "__main__":
    main()



'''
def read_files(directory):
    return [f"{directory}/{file}" for file in os.listdir(directory) if file.endswith(("csv",))]


def compress_files(paths, destination):
    for path in paths:
        print("Path", path)
        f = File(path, destination=destination)
        del f


def decompress_files(directory, destination):
    for path in os.listdir(directory):
        f = File(f"{directory}/{path}", compression=False, destination=destination)
        del f


def process_images(directory, output, decompressed_output):
    # Read Files
    cattle = read_files(directory)
    
    # Compression
    compress_files(cattle, output)
    decompress_files(output, decompressed_output)
'''