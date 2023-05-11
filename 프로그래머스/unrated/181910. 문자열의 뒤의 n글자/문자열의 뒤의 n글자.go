func solution(my_string string, n int) string {
    length := len(my_string)
    return my_string[length - n:]
}