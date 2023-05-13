def solution(myString):
    answer = [i for i in myString.strip('x').split('x') if i]
    return sorted(answer)