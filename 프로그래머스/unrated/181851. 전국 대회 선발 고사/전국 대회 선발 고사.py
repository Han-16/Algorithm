def solution(rank, attendance):
    true_list = []
    for i in sorted(rank):
        if attendance[rank.index(i)]:
            if len(true_list) == 2:
                true_list.append(rank.index(i))
                break
            else:
                true_list.append(rank.index(i))
    a, b, c = true_list
    return 10_000 * a + 100 * b + c