def solution(myString, pat):
    cnt = 0
    start = 0
    while True:
        index = myString.find(pat, start)
        if index == -1:
            break
        cnt += 1
        start = index + 1
    return cnt