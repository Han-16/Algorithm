def solution(arr, k):
    answer = []
    for i in arr:
        if i not in answer:
            if len(answer) < k:
                answer.append(i)
    for i in range(k - len(answer)):
        answer.append(-1)
    return answer