def solution(num_list):
    count = 0
    for i in num_list:
        while i != 1:
            if i % 2:
                i = (i-1) / 2
                count += 1
            else:
                i /= 2
                count += 1
    return count