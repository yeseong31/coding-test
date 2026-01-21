import java.util.Arrays;

public class Solution {
    
    public static int[] solution(int n, int s) {
        
        if (n > s) {
            return new int[]{-1};
        }

        int[] answer = new int[n];
        int base = s / n;
        
        Arrays.fill(answer, base);

        int remain = s % n;
        int idx = n;
        
        for (int i = 0; i < remain; i++) {
            answer[--idx] += 1;
        }

        return answer;
    }
}