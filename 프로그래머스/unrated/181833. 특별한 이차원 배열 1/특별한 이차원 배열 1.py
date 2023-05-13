def solution(n):
    answer = []
    for i in range(n):
        elem_list = []
        for j in range(n):
            if i == j:
                elem_list.append(1)
            else:
                elem_list.append(0)
        answer.append(elem_list)
    return answer