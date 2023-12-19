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
        try:
            m = data[i] - data[i-1]
        except IndexError:
            m = 0
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



