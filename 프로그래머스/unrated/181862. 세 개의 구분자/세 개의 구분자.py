def solution(myStr):
    split_str = 'abc'
    split_list = "".join(["@" if i in split_str else i for i in myStr])
    split_list = split_list.split('@')
    answer = [i for i in split_list if i]
    return answer if answer else ["EMPTY"]