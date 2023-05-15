def solution(arr):
    cnt_2 = arr.count(2)
    if cnt_2 == 0:
        return [-1]
    elif cnt_2 == 1:
        return [2]
    else:
        start = arr.index(2)
        end = arr[::-1].index(2)
        return arr[start:-end] if end != 0 else arr[start:]
    