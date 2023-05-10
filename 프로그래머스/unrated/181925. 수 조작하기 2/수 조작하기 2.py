def solution(numLog):
    answer = ""
    dict_ = dict(zip([1, -1, 10, -10], ["w", "s", "d", "a"]))
    for i in range(len(numLog) - 1):
        answer += dict_[numLog[i+1] - numLog[i]]
    return answer