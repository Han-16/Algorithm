class Solution {
    public int solution(int N, int A, int B) {
        int cnt = 0;
        while (A != B) {
            if (A % 2 == 0) {
                A /= 2;
            } else {
                A = A / 2 + 1;
            }
            if (B % 2 == 0) {
                B /= 2;
            } else {
                B = B / 2 + 1;
            }
            cnt++;
        }
        return cnt;
    }
}