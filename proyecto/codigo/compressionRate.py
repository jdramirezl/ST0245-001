import os
import numpy as np



def compressionRate(inputDir, outputDir):
    inputAvg = np.mean([os.path.getsize(os.path.join(inputDir, file))
                        for file in os.listdir(inputDir)])
    outAvg = np.mean([os.path.getsize(os.path.join(outputDir, file))
                      for file in os.listdir(outputDir)])
    return inputAvg, outAvg


def main():
    print(compressionRate(
        "./datasets/archivosCSV/ganado enfermo CSVs", "./Output/Compressed/Sick"))
    print(compressionRate("./datasets/archivosCSV/ganado sano CSVs",
                          "./Output/Compressed/Healthy"))

main()