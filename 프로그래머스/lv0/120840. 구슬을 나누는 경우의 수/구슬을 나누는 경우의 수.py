def solution(balls, share):
    return fact(balls) / (fact(balls - share) * fact(share))
               
        
def fact(n):
    if n == 1 or n == 0:
        return 1
    return n * fact(n-1)