def solution(age):
    # "a" == 97
    age = [int(i) for i in str(age)]
    answer = ""
    for i in age:
        answer += chr(i + 97)
    return answer
    