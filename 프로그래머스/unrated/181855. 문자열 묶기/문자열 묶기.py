def solution(strArr):
    preq = {}
    for i in strArr:
        if len(i) in preq.keys():
            preq[len(i)] += 1
        else:
            preq[len(i)] = 1
    return max(preq.values())