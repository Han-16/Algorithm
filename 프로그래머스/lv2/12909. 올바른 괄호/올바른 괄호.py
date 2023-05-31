def solution(s):
    stack = []
    for token in s:
        if token == ")":
            if stack:
                stack.pop()
            else:
                return False
        else:
            stack.append(token)
    return not stack