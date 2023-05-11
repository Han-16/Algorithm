func solution(start, end int) []int {
    answer := make([]int, end - start + 1)
    for i := start; i <= end; i++ {
        answer[i-start] = i
    }
    return answer
}