def solution(num_list):
    odd = 0
    even = 0
    for i, v in enumerate(num_list):
        if i % 2:
            odd += v
        else:
            even += v
    return max(odd, even)