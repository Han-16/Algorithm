def solution(n):
    count = 0  
    start = 1  
    end = 1    
    curr_sum = 1  

    while end <= n:  
        if curr_sum == n:  
            count += 1  
            curr_sum -= start
            start += 1  
        elif curr_sum < n:
            end += 1  
            curr_sum += end  
        else:  
            curr_sum -= start  
            start += 1  

    return count  
