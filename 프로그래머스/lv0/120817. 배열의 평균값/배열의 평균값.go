func solution(numbers []int) float64 {
    sum_ := 0
    for _, value := range numbers {
        sum_ += value
    }
    average := float64(sum_) / float64(len(numbers))
    return average
}