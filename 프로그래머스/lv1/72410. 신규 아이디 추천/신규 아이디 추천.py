def solution(new_id):
    id_list = list(new_id.lower())                # 1단계
    new_id = ''
    
    for i in id_list:                             # 2단계
        if i.isalpha() or i.isdigit() or i in ['-', '_', '.']:
            new_id += i
    
    while '..' in new_id:    # 3단계
        new_id = new_id.replace('..', '.')
    
    new_id = new_id.strip('.')                    # 4단계
    
    if not new_id:                                # 5단계
        new_id = 'a'
    
    if len(new_id) >= 16:                         # 6단계
        new_id = new_id[:15].strip('.')
    
    if len(new_id) <= 2:                          # 7단계
        while len(new_id) < 3:
            new_id = new_id + new_id[-1]
            
    return new_id