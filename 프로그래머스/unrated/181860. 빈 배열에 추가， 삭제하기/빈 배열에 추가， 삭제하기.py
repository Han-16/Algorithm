def solution(arr, flag):
    answer = []
    for i, v in enumerate(flag):
        if v:
            answer.extend([arr[i]] * arr[i] * 2)
        else:
            answer = answer[:len(answer) - arr[i]]
    return answer        