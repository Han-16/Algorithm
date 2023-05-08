def solution(a, d, included:list) -> int:
    sum = 0
    for i in range(len(included)):
        if included[i]:
            sum += a + (d * i)
            
    return sum