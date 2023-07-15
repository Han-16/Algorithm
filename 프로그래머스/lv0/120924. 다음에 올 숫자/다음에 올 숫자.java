class Solution {
    public int solution(int[] common) {
        int a = common[1] - common[0];
        int b = common[2] - common[1];
        int last = common[common.length - 1];
        return a == b ? last + a : last * (common[2] / common[1]);
        
    }
}
