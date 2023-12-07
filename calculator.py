import math


def computeMOCT(data):
    data = sorted(data)
    data_dict = {}
    mode = []    
    size = len(data)
    big = None


    for i in data:
        if i not in data_dict.keys():
            data_dict[i] = 0
    print(f"Mean: {round(sum(data)/size, 2)}")
    
    if size % 2 == 0:
        print(f"Median: {(data[math.trunc(size/2) - 1] + data[math.trunc(size/2)]) / 2}")
    else:
        print(f"Median: {data[len(data)/2]}")

    for i in data_dict.keys():
        for b in data:
            if i == b:
                data_dict[i] += 1

    for 
    print(f"Mode: {' '.join(mode)}")

    print(f"Min: {min(data)}")

    print(f"Max: {max(data)}")
    
    print(f"Range: {max(data) - min(data)}")

def main():
    n = input("Data: ").split(" ")
    n = [int(i) for i in n]
    computeMOCT(n)
    

main()
    