import java.util.Arrays;
import java.util.Queue;
import java.util.LinkedList;

class Solution {
    public int solution(int cacheSize, String[] cities) {
        
        if (cacheSize == 0) {
            return cities.length * 5;
        }
        
        cities = Arrays.stream(cities)
            .map(String::toLowerCase)
            .toArray(String[]::new);
        
        int runTime = 0;
        
        Queue<String> q = new LinkedList<>();
        
        for (String city: cities) {
            if (q.contains(city)) {
                runTime += 1;
                q.remove(city);
                q.add(city);
            } else {
                runTime += 5;
                if (q.size() < cacheSize) {
                    q.add(city);
                } else {
                    q.poll();
                    q.add(city);
                }
            }
        }
        return runTime;
    }
}