import java.util.*;

class Solution {
    
    public int solution(int alp, int cop, int[][] problems) {
        int n = problems.length;
        int[][] newProblems = new int[n + 2][5];
        for (int i = 0; i < n; i++) {
            newProblems[i] = problems[i];
        }
        newProblems[n] = new int[]{0, 0, 1, 0, 1};
        newProblems[n + 1] = new int[]{0, 0, 0, 1, 1};

        int maxAlp = 0, maxCop = 0;
        for (int[] p : newProblems) {
            maxAlp = Math.max(maxAlp, p[0]);
            maxCop = Math.max(maxCop, p[1]);
        }

        PriorityQueue<int[]> pq = new PriorityQueue<>(Comparator.comparingInt(a -> a[0]));
        Map<String, Integer> checked = new HashMap<>();

        pq.offer(new int[]{0, alp, cop});
        checked.put(alp + "," + cop, 0);

        int limit = 150;

        while (true) {
            int[] cur = pq.poll();
            int time = cur[0];
            int curAlp = cur[1];
            int curCop = cur[2];

            if (curAlp >= maxAlp && curCop >= maxCop) {
                return time;
            }

            for (int[] p : newProblems) {
                int alpReq = p[0], copReq = p[1];
                int alpRwd = p[2], copRwd = p[3], cost = p[4];

                if (curAlp < alpReq || curCop < copReq) continue;

                int nextCost = time + cost;
                int nextAlp = Math.min(curAlp + alpRwd, limit);
                int nextCop = Math.min(curCop + copRwd, limit);

                String key = nextAlp + "," + nextCop;

                if (checked.containsKey(key) && checked.get(key) <= nextCost) continue;

                checked.put(key, nextCost);
                pq.offer(new int[]{nextCost, nextAlp, nextCop});
            }
        }
    }
}