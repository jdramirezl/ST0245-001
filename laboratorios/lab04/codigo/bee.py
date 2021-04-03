
def binary(arr, x, index):
    l, r, i = 0, len(arr)-1, 0
    while l <= r:
        mid = l + (r - l) // 2
        if arr[mid][index] == x:
            return mid
        elif arr[mid][index] < x:
            l = mid + 1
        else:
            r = mid - 1
        i += 1
    
    
    return mid

def main():
    file = open("ConjuntoDeDatosCon1000000abejas.txt")
    bee_list = []
    result = {}
    
    for line in file:
        x, y, z = tuple(map(float, line.split(',')))
        bee_list.append((x,y,z))
    
    print(len(bee_list))
    
    bee_list.sort(key=lambda x: x[2])
    print("Start")
    
    count = 1
    for bee in bee_list:
        print("Alive with: "+ str(bee)+" in bee "+str(count))
        x, y, z = bee
        z_min = binary(bee_list, z - 100, 2)
        z_max = binary(bee_list, z + 100, 2)
        
        print("z_min",z_min,"z_max",z_max)
        
        bee_y = bee_list[z_min: z_max]
        bee_y.sort(key=lambda x: x[1])
        
        y_min = binary(bee_y, y - 100, 1)
        y_max = binary(bee_y, y + 100, 1)
        
        print("y_min",y_min,"y_max",y_max)
        
        bee_x = bee_y[y_min: y_max]
        bee_x.sort(key=lambda x: x[0])
        
        x_min = binary(bee_x, x - 100, 2)
        x_max = binary(bee_x, x + 100, 2)
        
        print("x_min",x_min,"x_max",x_max)
        
        result[bee] = bee_x[x_min: x_max]
        count += 1
    
    for bee in result:
        print("Key:",bee)
        print("Value:",result[bee])
        print()
    
    

if __name__ == "__main__":
    main()

