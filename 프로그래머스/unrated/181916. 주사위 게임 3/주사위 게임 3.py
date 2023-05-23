def solution(a, b, c, d):
    list_ = [a, b, c, d]
    dict_ = {}
    for i in list_:
        if i in dict_:
            dict_[i] += 1
        else:
            dict_[i] = 1
    sort_list = sorted(dict_.items(), key = lambda x: x[1], reverse = True)
    if len(sort_list) == 1:
        return 1111 * sort_list[0][0]
    elif len(sort_list) == 2:
        if sort_list[0][1] == 2:
            return (sort_list[0][0] + sort_list[1][0]) * abs(sort_list[0][0] - sort_list[1][0])
        else:
            return (10 * sort_list[0][0] + sort_list[1][0]) ** 2
    elif len(sort_list) == 3:
        return sort_list[1][0] * sort_list[2][0]
    else:
        return min(list_)