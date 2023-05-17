def solution(arr):
    sub = len(arr[0]) - len(arr)
    if sub > 0:
        for i in range(sub):
            arr.append([0 for j in range(len(arr[0]))])
    elif sub < 0:
        for i in arr:
            i.extend([0 for j in range(abs(sub))])
    elif sub == 0:
        return arr
    return arr