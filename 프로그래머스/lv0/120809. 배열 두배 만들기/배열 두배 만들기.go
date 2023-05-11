func solution(numbers []int) []int {
    for i, _ := range numbers {
        numbers[i] *= 2
    }
    return numbers
}