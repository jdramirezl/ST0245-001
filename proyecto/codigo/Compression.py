import Directory as d

if __name__ == "__main__":
    healthy_cows = d.Directory('datasets/archivosCSV/ganado sano CSVs')
    sick_cows = d.Directory('datasets/archivosCSV/ganado enfermo CSVs')
    healthy_cows_data = healthy_cows.files
    sick_cows_data = sick_cows.files
    
    for cow in healthy_cows_data[:5]:
        print("A cow: ", cow)
        print(cow.data[0][:10])
    