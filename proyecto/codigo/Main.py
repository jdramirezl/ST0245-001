import os
from .File import File


def read_files(directory):
    return [os.path.join(directory, file) for file in os.listdir(directory) if file.endswith(("csv",))]


def compress_files(paths, destination):
    for path in paths:
        f = File(path, destination=destination)
        del f


def decompress_files(directory, destination):
    for path in os.listdir(directory):
        f = File(os.path.join(destination, path), compression=False, destination=destination)
        del f


def process_images(directory, output, decompressed_output):
    # Read Files
    sick_cattle = read_files(directory)
    
    # Compression
    compress_files(sick_cattle, output)
    decompress_files(output, decompressed_output)


def main():
    # Process Sick
    directory = "datasets/archivosCSV/ganado enfermo CSVs"
    compressed_output = "datasets/Output/Compressed/Sick"
    decompressed_output = "datasets/Output/Decompressed/sick"
    process_images(directory, compressed_output, decompressed_output)
    
    # Process Healthy
    directory = "datasets/archivosCSV/ganado sano CSVs"
    compressed_output = "datasets/Output/Compressed/Healthy"
    decompressed_output = "datasets/Output/Decompressed/Healthy"
    process_images(directory, compressed_output, decompressed_output)


if __name__ == "__main__":
    main()
