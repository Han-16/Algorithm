def solution(numbers, hand):
    answer = ''
    distance = [[1,3],[0,0],[1,0],[2,0],[0,1],[1,1],[2,1],[0,2],[1,2],[2,2],[0,3],[2,3]]
    left_location = 10
    right_location = 11

    for i in numbers:
        if i in [1,4,7]:
            answer += 'L'
            left_location = i
        elif i in [3,6,9]:
            answer += 'R'
            right_location = i
        else:
            left_dist = (abs(distance[i][0] - distance[left_location][0]) + 
                     abs(distance[i][1] - distance[left_location][1]))
            right_dist = (abs(distance[i][0] - distance[right_location][0]) + 
                     abs(distance[i][1] - distance[right_location][1]))
            if left_dist > right_dist:
                answer += 'R'
                right_location = i  
            elif left_dist < right_dist:
                answer += 'L'
                left_location = i
            else:
                if hand == 'right':
                    answer += 'R'
                    right_location = i    
                else:
                    answer += 'L'
                    left_location = i
    return answer