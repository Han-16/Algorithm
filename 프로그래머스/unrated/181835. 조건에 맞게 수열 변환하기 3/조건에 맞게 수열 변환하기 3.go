func solution(arr []int, k int) []int {
    if k % 2 == 1 {
        for i, _ := range arr {
            arr[i] *= k
        }
    } else {
        for i, _ := range arr {
            arr[i] += k
        }
    }
    return arr
}