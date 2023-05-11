def solution(my_string:str, index_list:list) -> str:
    answer = ""
    for i in index_list:
        answer += my_string[i]
    return answer