def solution(a, b):
    if a % b == 0:
        return 1
    num = 1
    for i in range(min(a, b), 0, -1):
        if a % i == 0 and b % i == 0:
            num = i
            break
    b //= num 
    primes = []
    div = 2 
    while b > 1:
        if b % div == 0:
            primes.append(div)
            b //= div  
        else:
            div += 1
    lst = list(set(primes))
    return 1 if lst in [[2], [5], [2, 5]] else 2
