def solution(arr):
    cnt = 0
    cur = arr[:]
    while True:
        for i, v in enumerate(arr):
            if v >= 50 and not v % 2:
                arr[i] = v / 2
            elif v < 50 and v % 2:
                arr[i] = v * 2 + 1
        if cur == arr:
            return cnt
        else:
            cur = arr[:]
            cnt += 1
    