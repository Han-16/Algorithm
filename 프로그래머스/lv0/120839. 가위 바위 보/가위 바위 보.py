def solution(rsp):
    vsrsp = {"0":"5", "2":"0", "5":"2"}
    answer = ""
    for i in rsp:
        answer += vsrsp[i]
    return answer