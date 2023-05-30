def solution(n):
    i = 2
    while not n % i == 1:
        i += 1
    return i