import java.util.Arrays;

class Solution {
    public long solution(int n, int[] times) {
        long left = 0;
        long right = (long) Arrays.stream(times).max().getAsInt() * n;
        
        long answer = right;
        
        while (left <= right) {
            long mid = (left + right) / 2;
            
            long total = 0;
            for (int t : times) {
                total += mid / t;
            }
            
            if (total >= n) {
                answer = mid;
                right = mid - 1;
            } else {
                left = mid + 1;
            }
        }        
        
        return answer;
    }
}