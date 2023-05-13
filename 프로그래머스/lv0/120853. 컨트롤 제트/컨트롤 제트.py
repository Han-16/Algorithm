def solution(s):
    lst = s.split()
    sum_ = 0
    for i, v in enumerate(lst):
        if v == "Z":
            sum_ -= int(lst[i-1])
        else:
            sum_ += int(v)
    return sum_