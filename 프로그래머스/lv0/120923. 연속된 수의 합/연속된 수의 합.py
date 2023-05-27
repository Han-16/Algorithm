def solution(num, total):
    average = total // num
    if num % 2:
        return [i for i in range(average - num // 2, average - num // 2 + num)]
            
    else:
        return [i for i in range(average - (num // 2) + 1, average - (num // 2) + 1 + num)]