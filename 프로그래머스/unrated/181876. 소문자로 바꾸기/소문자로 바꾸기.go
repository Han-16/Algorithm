import "strings"

func solution(myString string) string {
    answer := ""
    for _, v := range myString {
        answer += strings.ToLower(string(v))
    }
    return answer
}