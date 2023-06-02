def solution(cards1, cards2, goal):
    answer = []
    c1 = 0
    c2 = 0
    while answer != goal:
        for i in goal:
            if c1 < len(cards1) and cards1[c1] == i:
                answer.append(cards1[c1])
                c1 += 1
            elif c2 < len(cards2) and cards2[c2] == i:
                answer.append(cards2[c2])
                c2 += 1
            else:
                return "No"
    return "Yes" 