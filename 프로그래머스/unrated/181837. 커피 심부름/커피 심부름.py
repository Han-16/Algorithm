def solution(order):
    sum_ = 0
    for i in order:
        if i == "anything":
            sum_ += 4_500
        elif "americano" in i:
            sum_ += 4_500
        elif "cafelatte" in i:
            sum_ += 5_000
    return sum_