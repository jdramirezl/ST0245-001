import RunLength as rl
import File as f



directory = "datasets/archivosCSV/ganado enfermo CSVs/cow-skinny.csv"
compressed_output = "Output/Compressed/Sick"
archivo = f.File(directory, True, compressed_output)

decompressed_input = "Output/Compressed/Sick/compressed-cow-skinny.csv"
decompressed_output = "Output/Decompressed/sick"
archivo = f.File(decompressed_input, False, decompressed_output)