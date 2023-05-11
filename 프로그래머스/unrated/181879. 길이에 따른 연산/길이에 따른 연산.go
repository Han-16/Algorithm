func solution(num_list []int) int {
    sum := 0
    mul := 1
    if len(num_list) >= 11 {
        for _, value := range num_list {
            sum += value
        } 
        return sum
    } else {
        for _, value := range num_list {
            mul *= value
        } 
        return mul
    }
    return 0
}