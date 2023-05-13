def solution(n):
    i = 1
    while factorial(i) <= n:
        i += 1
    return i - 1

def factorial(N):
    if N == 0:
        return 1
    return N * factorial(N-1)