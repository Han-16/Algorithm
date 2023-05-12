def solution(my_string):
    answer = ""
    for i in my_string:
        if my_string.count(i) >= 2 and i in answer:
            continue
        answer += i
    return answer
        