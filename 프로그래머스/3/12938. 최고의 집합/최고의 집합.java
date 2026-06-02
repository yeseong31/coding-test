import java.util.Arrays;

public class Solution {
    public int[] solution(int n, int s) {
        if (n > s) {
            return new int[]{-1};
        }

        int[] answer = new int[n];
        int base = s / n;
        int remainder = s % n;

        Arrays.fill(answer, base);

        for (int i = 0; i < remainder; i++) {
            answer[n - 1 - i]++;
        }

        return answer;
    }
}