def solution(n):
    fibo = [0, 1] 
    if n <= 1:
        return fibo[n]
    for i in range(2, n + 1):
        fibo.append(fibo[i-1] + fibo[i-2])
    return fibo[n] % 1234567