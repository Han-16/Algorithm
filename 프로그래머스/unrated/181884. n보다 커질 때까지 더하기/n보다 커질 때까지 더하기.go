func solution(numbers []int, n int) int {
    sum_ := 0
    for _, value := range numbers {
        sum_ += value
        if sum_ > n {
            return sum_
        }
    }
    return sum_
}