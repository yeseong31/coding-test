import java.util.Arrays;

class Solution {
    
    public int solution(int[][] targets) {
        int answer = 0;
        int n = targets.length;
        
        Arrays.sort(targets, (a, b) -> Integer.compare(a[0], b[0]));
        
        int idx = n - 1;
        
        while (idx >= 0) {
            int start = targets[idx][0];
            while (idx >= 0 && start < targets[idx][1]) {
                idx--;
            }
            answer++;
        }
            
        return answer;
    }
}