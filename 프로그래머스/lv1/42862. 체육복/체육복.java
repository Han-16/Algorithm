import java.util.Arrays;

public class Solution {

    public int solution(int n, int[] lost, int[] reserve) {
        int[] students = new int[n + 1]; 
        Arrays.fill(students, 1); 

        for (int lostStudent : lost) {
            students[lostStudent]--;
        }

        for (int reserveStudent : reserve) {
            students[reserveStudent]++;
        }

        for (int i = 1; i <= n; i++) {
            if (students[i] == 0) { 
                if (i > 1 && students[i - 1] > 1) { 
                    students[i]++;
                    students[i - 1]--;
                } else if (i < n && students[i + 1] > 1) { 
                    students[i]++;
                    students[i + 1]--;
                }
            }
        }

        int answer = (int) Arrays.stream(students)
                    .filter(count -> count > 0)
                    .count() - 1;
        
        return answer;
    }
}