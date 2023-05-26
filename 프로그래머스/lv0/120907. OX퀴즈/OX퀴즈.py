def solution(quiz):
    result = []
    for elem in quiz:
        x, operator, y, _, z = elem.split()
        x, y, z = int(x), int(y), int(z)
        if operator == '+':
            result.append("O") if x + y == z else result.append("X")
        else:
            result.append("O") if x - y == z else result.append("X")
    return result