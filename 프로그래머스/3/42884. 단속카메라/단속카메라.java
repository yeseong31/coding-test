import java.util.Arrays;

class Solution {
    public int solution(int[][] routes) {
        int answer = 0;
        int target = Integer.MIN_VALUE;
        
        Arrays.sort(routes, (a, b) -> a[1] - b[1]);
        
        for (int[] route : routes) {
            if (target < route[0]) {
                answer++;
                target = route[1];
            }
        }
        
        return answer;
    }
}