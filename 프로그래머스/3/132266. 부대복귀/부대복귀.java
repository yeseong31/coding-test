import java.util.*;

class Solution {

    public int[] solution(int n, int[][] roads, int[] sources, int destination) {
        List<int[]>[] graph = new List[n + 1];
        for (int i = 0; i <= n; i++) graph[i] = new ArrayList<>();

        for (int[] road : roads) {
            graph[road[0]].add(new int[]{road[1], 1});
            graph[road[1]].add(new int[]{road[0], 1});
        }

        int[] dist = new int[n + 1];
        Arrays.fill(dist, Integer.MAX_VALUE);
        dist[destination] = 0;

        PriorityQueue<int[]> pq = new PriorityQueue<>(Comparator.comparingInt(a -> a[0]));
        pq.offer(new int[]{0, destination});

        while (!pq.isEmpty()) {
            int[] cur = pq.poll();
            int d = cur[0], now = cur[1];

            if (dist[now] < d) continue;

            for (int[] next : graph[now]) {
                int cost = d + next[1];
                if (cost < dist[next[0]]) {
                    dist[next[0]] = cost;
                    pq.offer(new int[]{cost, next[0]});
                }
            }
        }

        int[] answer = new int[sources.length];
        for (int i = 0; i < sources.length; i++) {
            answer[i] = dist[sources[i]] == Integer.MAX_VALUE ? -1 : dist[sources[i]];
        }
        return answer;
    }
}