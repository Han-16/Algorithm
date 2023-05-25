def solution(babbling):
    can_pron = ["aya", "ye", 'woo', 'ma']
    answer = []
    for i in can_pron:
        for idx, v in enumerate(babbling):
            if i in v:
                babbling[idx] = v.replace(i, ',')
    cnt = 0
    for i in babbling:
        if set(i) == {','}:
            cnt += 1
    return cnt