def solution(my_string, s, e):
    answer = list(my_string)
    if s == 0:
        answer[:e+1] = answer[e::-1]
    else:
        answer[s:e+1] = answer[e:s-1:-1]
    return "".join(answer)