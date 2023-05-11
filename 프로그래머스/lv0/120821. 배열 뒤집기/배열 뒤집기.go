func solution(num_list []int) []int {
	var answer []int
	for i := len(num_list) - 1; i >= 0; i-- {
		answer = append(answer, num_list[i])
	}
	return answer
}   