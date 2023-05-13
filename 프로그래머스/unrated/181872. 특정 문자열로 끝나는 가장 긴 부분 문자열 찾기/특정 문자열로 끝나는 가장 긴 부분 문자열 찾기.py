def solution(myString, pat):
    myString = "".join(reversed(myString))
    pat = "".join(reversed(pat))
    
    answer = myString[myString.index(pat):]
    return "".join(reversed(answer))