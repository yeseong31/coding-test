import java.util.*;

class Solution {

    public long solution(int n, int[] works) {
        PriorityQueue<Integer> pq = new PriorityQueue<>(Collections.reverseOrder());
        for (int w : works) if (w > 0) pq.offer(w);

        while (n-- > 0 && !pq.isEmpty()) {
            int top = pq.poll();
            if (top == 0) break;
            pq.offer(top - 1);
        }

        long sum = 0;
        for (int v : pq) sum += (long) v * v;
        return sum;
    }
}