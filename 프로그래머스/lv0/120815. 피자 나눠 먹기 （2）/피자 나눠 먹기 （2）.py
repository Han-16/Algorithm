def solution(n):
    piece = 6
    pan = 1
    while piece * pan % n:
        pan += 1
    return pan