import java.util.*;

class Solution {

    private static final int[][] SCORES = {{1,1,1},{5,1,1},{25,5,1}};
    private static final Map<String, Integer> CHOICE = Map.of(
            "diamond", 0, "iron", 1, "stone", 2);

    public int solution(int[] picks, String[] minerals) {
        int answer = Integer.MAX_VALUE;
        // 상태: i, c, total, pick[0], pick[1], pick[2]
        Queue<int[]> q = new ArrayDeque<>();
        q.offer(new int[]{0, -1, 0, picks[0], picks[1], picks[2]});

        while (!q.isEmpty()) {
            int[] cur = q.poll();
            int i = cur[0], c = cur[1], total = cur[2];
            int[] pick = {cur[3], cur[4], cur[5]};

            if (c >= 0) pick[c]--;

            int pickSum = pick[0] + pick[1] + pick[2];
            if (i >= minerals.length || pickSum == 0) {
                answer = Math.min(answer, total);
                continue;
            }

            for (int a = 0; a < 3; a++) {
                if (pick[a] == 0) continue;
                int res = 0;
                for (int b = i; b < Math.min(i + 5, minerals.length); b++) {
                    res += SCORES[a][CHOICE.get(minerals[b])];
                }
                q.offer(new int[]{i + 5, a, total + res, pick[0], pick[1], pick[2]});
            }
        }

        return answer;
    }
}