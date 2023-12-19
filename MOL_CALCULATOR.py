import numpy as np




def ComputeDecile(data, k):
    k = k * 10
    p = k / 100
    K = len(data) + 1
    K *= p
    i = int(K)
    d = K % 1
    if d > 0:
        print(i)
        m = data[i] - data[i-1]
        t = round(m * d, 2)
        ans = round(data[i-1] + t, 2)
        return ans, False
    else:
        return round(K, 2), True 


def ComputePercentile(data, k):
    p = k / 100
    K = len(data) + 1
    K *= p
    i = int(K)
    d = K % 1
    if d > 0:
        print(i)
        m = data[i] - data[i-1]
        t = round(m * d, 2)
        ans = round(data[i-1] + t, 2)
        return ans, False
    else:
        return round(K, 2), True 

def ComputeQuartile(data, k):
    if k == "1":
        p = 0.25
    elif k == "2":
        p = 0.50
    elif k == "3":
        p = 0.75
    
    K = len(data) + 1
    K *= p
    i = int(K)
    d = K % 1
    if d > 0:
        print(i)
        m = data[i] - data[i-1]
        t = round(m * d, 2)
        ans = round(data[i-1] + t, 2)
        return ans, False
    else:
        return round(K), True 




# data = input("INPUT: ")
# n = float(input("N: "))
# data = data.split(" ")
# data = [float(x) for x in data]
# sorted_data = sorted(data)


# MOL_calc = MOL_CALC()
# ans, flag = MOL_CALC.Percentile(data=sorted_data, k=n)
# if flag == True:
#     print(f"Answer: {ans}")
#     print(f"The value in the dataset at that location: {sorted_data[round(ans)-1]}")
# else:
#     print(f"Answer: {ans}")


