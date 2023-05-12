import copy
def solution(strArr):
    answer = copy.deepcopy(strArr)
    for i in strArr:
        if "ad" in i:
            answer.remove(i)
    return answer