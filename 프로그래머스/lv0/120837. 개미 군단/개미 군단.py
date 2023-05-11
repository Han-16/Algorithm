def solution(hp):
    attack_stat = [5, 3, 1]
    count = 0
    for i in attack_stat:
        count += hp // i
        hp %= i
    return count