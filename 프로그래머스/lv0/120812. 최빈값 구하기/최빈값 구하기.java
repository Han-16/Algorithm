import java.util.*;

class Solution {
    public int solution(int[] array) {
        Map<Integer, Integer> map = new HashMap<>();
        int maxCount = 0;
        int answer = 0;
        
        for (int i : array) {
            if (map.containsKey(i)) {
                map.put(i, map.get(i) + 1);
            } else {
                map.put(i, 1);
            }
            
            int count = map.get(i);
            if (count > maxCount) {
                maxCount = count;
                answer = i;
            } else if (count == maxCount) {
                answer = -1; 
            }
        }
        
        return answer;
    }
}
