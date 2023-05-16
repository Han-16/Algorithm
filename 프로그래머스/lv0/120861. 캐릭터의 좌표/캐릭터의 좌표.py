def solution(keyinput, board):
    x, y = 0, 0
    x_max, y_max = board[0] // 2, board[1] // 2
    x_min, y_min = -(board[0] // 2), -(board[1] // 2)
    for i in keyinput:
        if i == "left":
            if x > x_min: 
                x -= 1
        elif i == "right":
            if x < x_max:
                x += 1
        elif i == "up":
            if y < y_max:
                y += 1
        elif i == "down":
            if y > y_min:
                y -= 1
    return [x, y]