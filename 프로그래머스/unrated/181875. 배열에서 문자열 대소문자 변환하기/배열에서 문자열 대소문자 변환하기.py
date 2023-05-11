def solution(strArr):
    return [v.upper() if i % 2 else v.lower() for i, v in enumerate(strArr)]