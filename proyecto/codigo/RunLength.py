


class RunLength:
    @staticmethod
    def compress(input):
        compressed_data = []
        for x in range(len(input)):
            curr_row = input[x]
            n = len(curr_row)
            i = 0
            output = []
            while i <= n - 1:
                count = 1
                while (i < n - 1 and curr_row[i] == curr_row[i + 1]):
                    count += 1
                    i += 1
                i += 1
                
                if count > 1:
                    output.append("#"+str(count))
                output.append(curr_row[i - 1])  
            
            compressed_data.append(output)

        return compressed_data


    @staticmethod
    def decompress(decode):
        decompressed_data = []
        
        for x in range(len(decode)):
            curr_row = decode[x]
            length = len(curr_row)
            i = 0
            output = []
            
            while i < length:
                times = curr_row[i]
                if times[0] == '#':
                    element = int(float(curr_row[i+1]))
                    times = int(times[1:])
                    for j in range(times):
                        output.append(element)
                    i += 1
                else:
                    output.append(int(float(times)))
                
                i += 1
            
            decompressed_data.append(output)
        
        return decompressed_data
