def solution(todo_list:list, finished:bool) -> str:
    return [v for i, v in enumerate(todo_list) if not finished[i]]