def solution(l, r):
    result = []
    for i in range(l, r+1):
        if i % 5 == 0:
            if not str(i).replace('5', '').replace('0',''):
                result.append(i)
    return result if result else [-1]