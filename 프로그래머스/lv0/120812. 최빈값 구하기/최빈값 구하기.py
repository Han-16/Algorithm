def solution(array):
    dict_ = {}
    answer = 0
    
    for i in array:
        if i in dict_:
            dict_[i] += 1
        else:
            dict_[i] = 1

    for i in dict_:
        if dict_[i] == max(dict_.values()):
            if answer != 0:
                return -1
            answer = i
    return answer
