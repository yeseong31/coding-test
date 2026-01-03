import java.util.*;

class Solution {
    
    public int solution(int[][] scores) {
        int[] answer = scores[0];

        Arrays.sort(scores, (a, b) -> {
            if (a[0] != b[0]) {
                return b[0] - a[0];
            }
            return a[1] - b[1];
        });

        int max = 0;
        int rank = 1;

        for (int[] score : scores) {
            int w = score[0];
            int p = score[1];

            if (answer[0] < w && answer[1] < p) {
                return -1;
            }

            if (max > p) {
                continue;
            }

            if (answer[0] + answer[1] < w + p) {
                rank++;
            }

            max = p;
        }

        return rank;
    }
}