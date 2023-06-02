def solution(survey, choices):
    score_dict = {'R':0, 'T':0, 'C':0, 'F':0, 'J':0, 'M':0, 'A':0, 'N':0}
    answer = ''
    for i, v in enumerate(choices):
        if (score := v - 4) > 0:
            score_dict[survey[i][1]] += score
        else:
            score_dict[survey[i][0]] += abs(score)
    
    answer += 'R' if score_dict['R'] >= score_dict['T'] else 'T'
    answer += 'C' if score_dict['C'] >= score_dict['F'] else 'F'
    answer += 'J' if score_dict['J'] >= score_dict['M'] else 'M'
    answer += 'A' if score_dict['A'] >= score_dict['N'] else 'N'
    
    return answer