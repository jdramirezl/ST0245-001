
# TODO: CHANGE 1'S TO CHAR


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
                
                output.append(count)
                output.append(curr_row[i - 1])  
            
            compressed_data.append(output)

        return compressed_data


    @staticmethod
    def decompress(decode):
        decompressed_data = []
        
        for x in range(len(decode)):
            curr_row = decode[x]
            
            output = []
            for i in range(0, len(curr_row), 2):
                num = curr_row[i]
                element = curr_row[i+1]

                for j in range(num):
                    output.append(element)
            
            decompressed_data.append(output)
        
        return decompressed_data
