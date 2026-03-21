import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;
import java.util.Queue;

public class Solution {

    private static List<List<Edge>> graph = new ArrayList<>();
    private static int answer = 1;

    public int solution(int n, int infection, int[][] edges, int k) {
        graph = new ArrayList<>();
        for (int i = 0; i <= n; i++) {
            graph.add(new ArrayList<>());
        }

        for (int[] edge : edges) {
            int x = edge[0];
            int y = edge[1];
            int t  = edge[2];
            graph.get(x).add(new Edge(y, t));
            graph.get(y).add(new Edge(x, t));
        }

        boolean[] infected = new boolean[n + 1];
        infected[infection] = true;

        dfs(0, n, k, infected);

        return answer;
    }

    private static void dfs(int step, int n, int k, boolean[] infected) {
        int count = 0;

        for (boolean b : infected) {
            if (b) count++;
        }

        answer = Math.max(answer, count);

        if (step == k) return;

        for (int type = 1; type <= 3; type++) {
            boolean[] next = bfs(n, infected, type);
            dfs(step + 1, n, k, next);
        }
    }

    private static boolean[] bfs(int n, boolean[] infected, int type) {
        boolean[] next = infected.clone();
        Queue<Integer> queue = new LinkedList<>();

        for (int i = 1; i <= n; i++) {
            if (infected[i]) queue.offer(i);
        }

        while (!queue.isEmpty()) {
            int curr = queue.poll();
            for (Edge e : graph.get(curr)) {
                if (e.type == type && !next[e.to]) {
                    next[e.to] = true;
                    queue.offer(e.to);
                }
            }
        }

        return next;
    }

    private static class Edge {
        private final int to;
        private final int type;

        public Edge(int to, int type) {
            this.to = to;
            this.type = type;
        }
    }
}
