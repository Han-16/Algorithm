import math
def solution(my_str:str, n:str) -> list:
    answer = []
    my_str = list(my_str)
    for i in range(math.ceil(len(my_str) / n)):
        answer.append("".join(my_str[:n]))
        my_str = my_str[n:]
    return answer