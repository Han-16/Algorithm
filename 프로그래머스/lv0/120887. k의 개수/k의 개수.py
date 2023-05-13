def solution(i, j, k):
    num_list = [str(num) for num in range(i, j + 1)]
    count = 0
    k = str(k)
    
    for elem in num_list:
        for num in elem:
            if num == k:
                count += 1
    return count