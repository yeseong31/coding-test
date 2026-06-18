import java.util.*;

class Solution {

    public int solution(int distLimit, int splitLimit) {
        long d = distLimit;
        long s = splitLimit;

        List<Long> values = new ArrayList<>();
        generate(1, s, values);
        Collections.sort(values);

        int n = values.size();
        long[] cost = new long[n];
        Arrays.fill(cost, Long.MAX_VALUE);
        cost[0] = 0;

        Map<Long, Integer> index = new HashMap<>(n);
        for (int i = 0; i < n; i++) {
            index.put(values.get(i), i);
        }

        for (int i = 0; i < n; i++) {
            long p = values.get(i);

            if (cost[i] == Long.MAX_VALUE) {
                continue;
            }

            if (p * 2 <= s) {
                int next = index.get(p * 2);
                cost[next] = Math.min(cost[next], cost[i] + p);
            }

            if (p * 3 <= s) {
                int next = index.get(p * 3);
                cost[next] = Math.min(cost[next], cost[i] + p);
            }
        }

        long answer = 1;

        for (int i = 0; i < n; i++) {
            long p = values.get(i);

            if (cost[i] > d) {
                continue;
            }

            answer = Math.max(answer, p);

            long remain = d - cost[i];
            long x = Math.min(p, remain);

            if (p * 2 <= s) {
                answer = Math.max(answer, p + x);
            }

            if (p * 3 <= s) {
                answer = Math.max(answer, p + (x << 1));
            }
        }

        return (int) answer;
    }

    private void generate(long value, long limit, List<Long> values) {
        if (value > limit) {
            return;
        }

        values.add(value);
        generate(value * 2, limit, values);
        generate(value * 3, limit, values);
    }
}