def solution(num, k):
    num, k = map(str, [num, k])
    return num.index(k)+1 if k in num else -1