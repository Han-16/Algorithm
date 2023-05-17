def solution(n):
    number = 0
    for i in range(n):
        while True:
            if "3" in str(number + 1) or (number+1) % 3 == 0:
                number += 1
                continue
            number += 1
            break
    return number