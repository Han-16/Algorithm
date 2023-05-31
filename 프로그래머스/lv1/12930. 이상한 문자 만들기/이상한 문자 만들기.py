def solution(s):
    replace = s.replace(" ", "@")
    s_list = [i for i in replace[1:]]
    string = []
    answer = []
    word = f"{replace[0]}"
    
    for i in s_list:
        if i == "@":
            if i in word:
                word += i
            else:
                string.append(word)
                word = i
        else:
            if '@' in word:
                string.append(word)
                word = i
            else:
                word += i
    string.append(word)
        
    
    for i, v in enumerate(string):
        if "@" in v:
            string[i] = v
        else:
            temp = ""
            for idx, val in enumerate(v):
                if idx % 2:
                    temp += val.lower()
                else:
                    temp += val.upper()
            string[i] = temp
    return "".join(string).replace("@", " ")