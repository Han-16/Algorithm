def solution(my_string):
    ALPHA = {chr(i) : 0 for i in range(ord('A'), ord('Z') + 1)}
    alpha = {chr(i) : 0 for i in range(ord('a'), ord('z') + 1)}
    
    for i in my_string:
        if i.isupper():
            ALPHA[i] += 1
        else:
            alpha[i] += 1
            
    return list(ALPHA.values()) +list(alpha.values())