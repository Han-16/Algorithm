def solution(arr):
    answer = True
    for i in range(len(arr)):
        for j in range(len(arr)):
            if arr[i][j] == arr[j][i]:
                continue
            answer = False
    return int(answer)