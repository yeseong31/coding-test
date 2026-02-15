import java.util.*;

class Solution {

    private int maxGap = -1;
    private int[] answer = {-1};

    public int[] solution(int n, int[] info) {
        int[] ryan = new int[11];
        dfs(n, 0, ryan, info);
        return answer;
    }

    private void dfs(int remain, int start, int[] ryan, int[] info) {
        if (remain == 0) {
            int[] candidate = Arrays.copyOf(ryan, 11);
            int[] scores = getScores(info, candidate);

            int apeach = scores[0];
            int ryanScore = scores[1];

            if (ryanScore > apeach) {
                int gap = ryanScore - apeach;

                if (gap > maxGap) {
                    maxGap = gap;
                    answer = candidate;
                } else if (gap == maxGap) {
                    if (isBetter(candidate, answer)) {
                        answer = candidate;
                    }
                }
            }
            return;
        }

        for (int i = start; i < 11; i++) {
            ryan[i]++;
            dfs(remain - 1, i, ryan, info);
            ryan[i]--;
        }
    }

    private int[] getScores(int[] apeachBoard, int[] ryanBoard) {
        int apeachScore = 0;
        int ryanScore = 0;

        for (int i = 0; i < 11; i++) {
            int score = 10 - i;

            if (apeachBoard[i] == 0 && ryanBoard[i] == 0) continue;

            if (apeachBoard[i] >= ryanBoard[i]) {
                apeachScore += score;
            } else {
                ryanScore += score;
            }
        }

        return new int[]{apeachScore, ryanScore};
    }

    private boolean isBetter(int[] a, int[] b) {
        for (int i = 10; i >= 0; i--) {
            if (a[i] != b[i]) {
                return a[i] > b[i];
            }
        }
        return false;
    }
}