def solution(board, k):
    sum_ = 0
    for i in range(len(board)):
        for j in range(len(board[i])):
            if i + j <= k:
                sum_+= board[i][j]
    return sum_