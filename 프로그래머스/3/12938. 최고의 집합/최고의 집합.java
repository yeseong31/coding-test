import java.util.Arrays;

class Solution {

    public int[] solution(int n, int s) {
        if (s < n) {
            return new int[]{-1};
        }

        int quotient = s / n;
        int remainder = s % n;

        int[] answer = new int[n];
        Arrays.fill(answer, quotient);

        for (int i = n - remainder; i < n; i++) {
            answer[i]++;
        }

        return answer;
    }
}