def solution(my_strings, parts):
    answer = ""
    for i, v in enumerate(my_strings):
        start, end = parts[i]
        print(start, end)
        answer += v[start:end+1]
    return answer
    