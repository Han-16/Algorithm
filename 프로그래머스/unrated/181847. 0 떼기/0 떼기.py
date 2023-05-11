def solution(n_str:str):
    str_list = list(n_str)    
    for i, v in enumerate(str_list):
        if v != "0":
            return "".join(str_list[i:])