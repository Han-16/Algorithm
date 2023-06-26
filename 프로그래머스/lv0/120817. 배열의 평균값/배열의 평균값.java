class Solution {
    double solution(int[] numbers) {
        double answer, sum = 0;
        for (int i: numbers) {
            sum += i;
        }
        answer = sum / numbers.length;
        return answer;
    }
}