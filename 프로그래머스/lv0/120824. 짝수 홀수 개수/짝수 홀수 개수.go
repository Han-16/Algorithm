func solution(num_list []int) [2]int {
    var answer [2]int
    for _, value := range num_list {
        answer[value % 2]++
    }
    return answer
}