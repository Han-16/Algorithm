def solution(arr, queries):
    answer = []
    for s, e, k in queries:
        flag = True
        for i in sorted(arr[s:e+1]):
            if i > k:
                answer.append(i)
                flag = False    
                break
        if flag:
            answer.append(-1)
    return answer