import java.util.HashSet;

class Solution {
    public int solution(int[] elements) {
        int n = elements.length;
        HashSet<Integer> set = new HashSet<>();

        for (int i = 0; i < n; i++) {
            int sum = 0;
            for (int j = i; j < i + n; j++) {
                sum += elements[j % n];
                set.add(sum);
            }
        }

        return set.size();
    }
}