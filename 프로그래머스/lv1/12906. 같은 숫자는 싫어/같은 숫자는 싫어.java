import java.util.*;

class Solution { 
    public ArrayList<Integer> solution(int[] arr) {
        ArrayList<Integer> answer = new ArrayList<>();
        int prev = -1;
        
        for (int i : arr) {
            if (i == prev) {
                continue;
            } else {
                answer.add(i);
                prev = i;
            }
        }
        return answer;
    }
}