def solution(binomial:str) -> int:
    lst = binomial.split()
    expression = lst[1]
    
    if expression == "+":
        return int(lst[0]) + int(lst[2])
    elif expression == "-":
        return int(lst[0]) - int(lst[2])
    else:
        return int(lst[0]) * int(lst[2])