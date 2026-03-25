class Solution {
    
    public int[] solution(int n, long left, long right) {
        int size = (int)(right - left + 1);
        int[] answer = new int[size];
        
        int idx = 0;
        for (long v = left; v <= right; v++) {
            answer[idx++] = (int)(Math.max(v / n, v % n) + 1);
        }
        
        return answer;
    }
}