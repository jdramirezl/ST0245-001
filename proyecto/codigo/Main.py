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


if __name__ == "__main__":
    main()
