def solution(a, b, c):
    sum = 1
    dict = {key: 0 for key in range(1, 7)}
    tup = a, b, c
    for i in tup:
        dict[i] += 1
        
    for i in dict.values():
        if i == 3:
            return 3*a * 3*(a**2) * 3*(a**3)
        elif i == 2:
            return (a + b + c) * (a**2 + b**2 + c**2)
    
    return a + b + c
        