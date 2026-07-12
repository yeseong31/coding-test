import java.util.Arrays;

class Solution {

    public int[] solution(int n, int s) {
        if (n > s) return new int[]{-1};

        int[] answer = new int[n];
        Arrays.fill(answer, s / n);
        for (int i = n - (s % n); i < n; i++) answer[i]++;
        return answer;
    }
}