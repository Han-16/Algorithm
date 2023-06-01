def solution(name, yearning, photo):
    na_ye = {v : yearning[i] for i, v in enumerate(name)}
    answer = []
    for elem in photo:
        score = 0
        for name in elem:
            if name in na_ye:
                score += na_ye[name]
        answer.append(score)
    return answer