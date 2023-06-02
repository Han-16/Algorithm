def solution(n):
    if n == 0:
        return 0
    result = ''
    decimal = 0
    
    while n > 0:
        remainder = n % 3
        result = str(remainder) + result
        n = n // 3

    for i, v in enumerate(result):
        if int(v):
            decimal += 3 ** i * int(v)
    
    return decimal