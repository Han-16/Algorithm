def solution(numlist, n):
    lst = sorted([[abs(i - n), False] if i >= n else [abs(i - n), True] for i in numlist])
    return [n - elem[0] if elem[1] else n + elem[0] for elem in lst]