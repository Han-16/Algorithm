def solution(my_string, m:int, c:int) -> str:
    str_list = []
    for i in range(0, len(my_string), m):
        str_list.append(my_string[i:i+m])
    return "".join([i[c-1] for i in str_list])