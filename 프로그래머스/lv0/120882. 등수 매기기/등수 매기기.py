def solution(score):    
    answer = [(math + eng) / 2 for math, eng in score]
    return [sorted(answer, reverse=True).index(i)+1 for i in answer]