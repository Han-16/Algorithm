def solution(participant, completion):
    part_dict = {}
    for i in participant:
        if i in part_dict:
            part_dict[i] += 1
        else:
            part_dict[i] = 1
    
    for i in completion:
        part_dict[i] -= 1
        if part_dict[i] == 0:
            del part_dict[i]
    
    return "".join(list(part_dict.keys()))