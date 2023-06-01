def solution(s):
    answer = []
    for i, v in enumerate(s):
        prev = 0
        FLAG = False
        for index, token in enumerate(s[:i]):
            if token == v:
                prev = index
                if prev == 0:
                    FLAG = True
        if prev or FLAG:
            answer.append(i - prev)
        else:
            answer.append(-1)
    return answer