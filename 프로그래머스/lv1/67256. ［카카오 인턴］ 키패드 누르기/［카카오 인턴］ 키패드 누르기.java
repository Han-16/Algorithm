import java.util.HashMap;
import java.util.Map;

public class Solution {
    public static String solution(int[] numbers, String hand) {
        StringBuilder answer = new StringBuilder();
        int[][] distance = {{1,3},{0,0},{1,0},{2,0},{0,1},{1,1},{2,1},{0,2},{1,2},{2,2},{0,3},{2,3}};
        int leftLocation = 10;
        int rightLocation = 11;

        for (int i : numbers) {
            if (i == 1 || i == 4 || i == 7) {
                answer.append("L");
                leftLocation = i;
            } else if (i == 3 || i == 6 || i == 9) {
                answer.append("R");
                rightLocation = i;
            } else {
                int[] currentLocation = distance[i];
                int leftDistance = Math.abs(currentLocation[0] - distance[leftLocation][0])
                        + Math.abs(currentLocation[1] - distance[leftLocation][1]);
                int rightDistance = Math.abs(currentLocation[0] - distance[rightLocation][0])
                        + Math.abs(currentLocation[1] - distance[rightLocation][1]);

                if (leftDistance > rightDistance) {
                    answer.append("R");
                    rightLocation = i;
                } else if (leftDistance < rightDistance) {
                    answer.append("L");
                    leftLocation = i;
                } else {
                    if (hand.equals("right")) {
                        answer.append("R");
                        rightLocation = i;
                    } else {
                        answer.append("L");
                        leftLocation = i;
                    }
                }
            }
        }

        return answer.toString();
    }
}
