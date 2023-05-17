def solution(chicken):
    service = 0
    while chicken >= 10:
        chicken -= 9
        service += 1
    return service