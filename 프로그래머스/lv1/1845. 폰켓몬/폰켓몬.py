def solution(nums):
    dict_ = {}
    N = len(nums) / 2
    for i in nums:
        if i in dict_:
            dict_[i] += 1
        else:
            dict_[i] = 1
            
    if N <= len(dict_.keys()):
        return N
    return len(dict_.keys())