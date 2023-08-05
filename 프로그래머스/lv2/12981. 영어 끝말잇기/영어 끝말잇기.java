import java.util.HashMap;

class Solution {
    public int[] solution(int n, String[] words) {
        HashMap<String, Boolean> map = new HashMap<>();
        int[] result = new int[2];
        char prev = words[0].charAt(0);
        int lastIdx;
        
        for (int i = 0; i < words.length; i++) {
            if (words[i].charAt(0) != prev || map.containsKey(words[i]) || words[i].length() == 1) {
                result[0] = i % n + 1;
                result[1] = i / n + 1;
                return result;
            } else {
                map.put(words[i], true);
                lastIdx = words[i].length() - 1;
                prev = words[i].charAt(lastIdx);
                
            }
        }
        
        
        return result;
    }
}