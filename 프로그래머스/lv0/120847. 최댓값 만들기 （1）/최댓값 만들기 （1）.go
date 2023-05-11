import "sort"

func solution(numbers []int) int {
    sort.Ints(numbers)   
    max := numbers[len(numbers) - 1] * numbers[len(numbers) - 2]
    return max
}