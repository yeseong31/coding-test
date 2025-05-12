import java.util.Arrays;

class Solution {
    public long solution(int n, int[] times) {
        Arrays.sort(times);
        
        long minTime = 0;
        long maxTime = (long) times[times.length - 1] * n;
        long answer = maxTime;
        
        while (minTime < maxTime) {
            long currentTime = (minTime + maxTime) / 2;
            long required = 0;
            
            for (int t : times) {
                required += currentTime / t;
                if (required >= n) {
                    break;
                }
            }
            
            if (required >= n) {
                answer = Math.min(answer, currentTime);
                maxTime = currentTime;
            } else {
                minTime = currentTime + 1;
            }
        }
        
        return answer;
    }
}