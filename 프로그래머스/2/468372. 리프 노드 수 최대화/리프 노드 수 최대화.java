import java.util.*;

class Solution {
    
    public int solution(int dist_limit, int split_limit) {
        long D = dist_limit;
        long S = split_limit;

        List<Long> values = new ArrayList<>();
        Queue<Long> q = new ArrayDeque<>();
        Set<Long> visited = new HashSet<>();

        q.offer(1L);
        visited.add(1L);

        while (!q.isEmpty()) {
            long cur = q.poll();
            values.add(cur);

            if (cur * 2 <= S && visited.add(cur * 2)) {
                q.offer(cur * 2);
            }
            if (cur * 3 <= S && visited.add(cur * 3)) {
                q.offer(cur * 3);
            }
        }

        Collections.sort(values);

        Map<Long, Long> cost = new HashMap<>();
        for (long v : values) {
            cost.put(v, Long.MAX_VALUE);
        }
        cost.put(1L, 0L);

        for (long p : values) {
            long curCost = cost.get(p);
            if (curCost == Long.MAX_VALUE) continue;

            if (p * 2 <= S) {
                long next = p * 2;
                long nextCost = curCost + p;
                if (nextCost < cost.get(next)) {
                    cost.put(next, nextCost);
                }
            }

            if (p * 3 <= S) {
                long next = p * 3;
                long nextCost = curCost + p;
                if (nextCost < cost.get(next)) {
                    cost.put(next, nextCost);
                }
            }
        }

        long answer = 1;

        for (long p : values) {
            long curCost = cost.get(p);
            if (curCost > D) continue;

            answer = Math.max(answer, p);

            long remain = D - curCost;

            if (p * 2 <= S) {
                long x = Math.min(p, remain);
                answer = Math.max(answer, p + x);
            }

            if (p * 3 <= S) {
                long x = Math.min(p, remain);
                answer = Math.max(answer, p + 2 * x);
            }
        }

        return (int) answer;
    }
}