def solution(X, Y):
    x_set = set(X)
    zzac = {}
    for i in x_set:
        if (min_ := min(X.count(i), Y.count(i))) >= 1:
            zzac[i] = min_
    zzac = dict(sorted(zzac.items(), reverse = True))
    
    if zzac == {}:
        return '-1'
    elif list(zzac.keys()) == ['0']:
        return '0'
    
    answer = ''
    for k, v in zzac.items():
        answer += k * v
    return answer
    