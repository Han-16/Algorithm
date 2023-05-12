def solution(arr:list, delete_list:list):
    for i in delete_list:
        if i in arr:
            arr.remove(i)
    return arr