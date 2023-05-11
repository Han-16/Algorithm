def solution(numbers):
    numbers.sort()
    max_1 = numbers[-1] * numbers[-2]
    max_2 = numbers[0] * numbers[1]
    return max(max_1, max_2)