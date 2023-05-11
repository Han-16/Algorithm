func solution(n, k int) int {
    ggochi := 12000 * n
    free := n / 10
    bev := 2000 * (k - free)
    return ggochi + bev
}