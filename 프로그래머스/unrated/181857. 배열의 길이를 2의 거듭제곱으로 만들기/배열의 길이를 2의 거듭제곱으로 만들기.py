import math

def solution(arr):
    ex = math.ceil(math.log2(len(arr)))
    for i in range(2 ** ex - len(arr)):
        arr.append(0)
    return arr