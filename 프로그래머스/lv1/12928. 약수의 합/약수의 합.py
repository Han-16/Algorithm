def solution(n):
    answer = 0
    i = 1
    while i ** 2 <= n:
        if n % i == 0:
            if i == n//i:
                answer += i
            else:
                answer += i + (n // i)
        i += 1
            
    return answer