def solution(my_string):
    str_list = my_string.split()
    sum_ = int(str_list[0])
    str_list = str_list[1:]
    for i in range(0, len(str_list), 2):
        if str_list[i] == "+":
            sum_ += int(str_list[i+1])
        else:
            sum_ -= int(str_list[i+1])
    return sum_