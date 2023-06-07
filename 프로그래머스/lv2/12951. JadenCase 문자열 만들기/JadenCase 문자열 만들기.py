def solution(s):
    lst = []
    answer = ''
    
    for i in s.split(' '):
        if i != '' and i[0].isalpha:
            lst.append(i[0].upper() + i[1:].lower())
        else:
            lst.append(i.lower())
    for i in lst:
        answer += i + " "
        
    return answer[:-1]