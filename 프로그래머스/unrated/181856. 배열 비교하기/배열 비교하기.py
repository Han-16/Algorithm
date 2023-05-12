def solution(arr1, arr2) -> int:
    if len(arr1) == len(arr2):
        sum_1, sum_2 = sum(arr1), sum(arr2)
        if sum_1 > sum_2:
            return 1
        elif sum_1 < sum_2:
            return -1
        return 0
    
    elif len(arr1) > len(arr2):
        return 1
    return -1