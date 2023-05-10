def solution(n, control):
    dict_ = {"w" : 1, "s" : -1, "d" : 10, "a" : -10}
    for i in control:
        n += dict_[i]
    
    return n