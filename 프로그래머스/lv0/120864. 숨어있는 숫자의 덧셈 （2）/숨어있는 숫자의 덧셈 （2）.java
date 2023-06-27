class Solution {
    public int solution(String my_string) {
        int sum = 0;
        String s = my_string.replaceAll("[a-zA-Z]", " ");
        String[] split = s.split(" ");
        for (String i : split) {
            if (!i.equals("")) {
                sum += Integer.valueOf(i);
            }
        }
        return sum;
    }
}