def solution(k, m, score):
    score.sort(reverse = True)
    sum_ = 0
    for i in range(0, len(score), m):
        if len(score[i:i+m]) == m:
            sum_ += min(score[i:i+m]) * m
    return sum_