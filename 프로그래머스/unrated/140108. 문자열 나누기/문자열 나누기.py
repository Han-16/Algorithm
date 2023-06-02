def solution(s):
    
    split_cnt = 0
    first = s[0]
    same = 0
    diff = 0
    for i, v in enumerate(s):
        if v == first:
            same += 1
        else:
            diff += 1

        if same == diff:
            same = diff = 0
            split_cnt += 1
            if i == len(s) - 1:
                split_cnt -= 1
            else:
                first = s[i+1]
                
    split_cnt += 1    
    return split_cnt
