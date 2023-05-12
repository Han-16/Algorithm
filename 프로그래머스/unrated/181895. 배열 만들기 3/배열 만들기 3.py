def solution(arr, intervals):
    answer = []
    for i in intervals:
        start, end = i[0], i[1]+1
        answer.extend(arr[start:end])
    return answer