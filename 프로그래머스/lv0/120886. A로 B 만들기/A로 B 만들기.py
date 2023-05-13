def solution(before, after):
    before = list(before)
    after = list(after)
    before.sort()
    after.sort()
    
    return int(before == after)