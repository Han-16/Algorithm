def solution(box:list, n):
    x, y, z = box
    return (x // n) * (y // n) * (z // n)