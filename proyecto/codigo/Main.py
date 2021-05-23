import os
from File import File
from Images import Image
import tracemalloc
import time


def process(directory, output, compression):
    # Read Files
    files = [f"{directory}/{file}" for file in os.listdir(directory) if file.endswith(("csv",))]

    # Process
    for path in files:
        now = time.time()
        tracemalloc.start()
        
        f = File(path, compression=compression, destination=output)
        del f
        
        current, peak = tracemalloc.get_traced_memory()
        print(path, ",", peak/(10**6), ",", (time.time() - now )/1000, ',', os.path.getsize(path))
        # print(f"Current memory usage is {current / (10**6)}MB; Peak was {peak / (10**6)}MB")
        tracemalloc.stop()
        # print("TOTAL TIME:", )
        tracemalloc.reset_peak()



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
    
    
    '''
    image_output = "Images/Sick"
    Image(decompressed_output, image_output)
    '''
    
    
    # Process Healthy
    directory = "datasets/archivosCSV/ganado sano CSVs"
    compressed_output = "Output/Compressed/Healthy"
    decompressed_output = "Output/Decompressed/Healthy"

    process_images(directory, compressed_output, decompressed_output)
    
    
    '''
    image_output = "Images/Healthy"
    Image(decompressed_output, image_output)
    '''


if __name__ == "__main__":
    main()
