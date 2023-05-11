def solution(cipher:str, code:int) -> str:
    return cipher[code-1::code]