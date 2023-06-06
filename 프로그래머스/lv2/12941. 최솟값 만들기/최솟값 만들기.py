def solution(A, B):
    min_sum = 0
    for a, b in zip(sorted(A), sorted(B, reverse = True)):
        min_sum += a * b
    return min_sum