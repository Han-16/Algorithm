def solution(emergency):
    emer_list = sorted(emergency, reverse = True)
    return [emer_list.index(i) + 1 for i in emergency]