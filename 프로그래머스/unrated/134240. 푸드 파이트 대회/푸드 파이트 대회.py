def solution(food):
    food_dict = {}
    answer = ''
    for i in range(len(food)):
        food_dict[i] = food[i] // 2
        
    for i in food_dict:
        if i:
            answer += str(i) * food_dict[i]
    answer += '0' + answer[::-1]
    return answer