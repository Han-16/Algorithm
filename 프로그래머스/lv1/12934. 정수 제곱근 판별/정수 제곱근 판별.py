def solution(n):
    num = n ** (1/2)
    return (num + 1) ** 2 if num.is_integer() else -1