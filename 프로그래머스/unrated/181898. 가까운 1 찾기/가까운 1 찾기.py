def solution(arr:list, idx:int) -> int:
    return arr[idx:].index(1) + idx if 1 in arr[idx:] else -1    