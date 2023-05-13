def solution(my_string):
    buffer = ""
    answer = []
    for i in my_string:
        if i.isdigit():
            buffer += i
        else:
            if buffer:
                answer.append(int(buffer))
                buffer = ""
    if buffer:
        answer.append(int(buffer))
    return sum(answer)