def solution(array, n):
    array.sort()
    answer = array[0]
    for i in array:
        if i < n:
            answer = i
        else:
            if i - n < n - answer:
                return i
            return answer
    return answer