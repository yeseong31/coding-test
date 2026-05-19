import java.util.*;

public class Solution {
    
    private int maxInfected = 1;

    public int solution(int n, int infection, int[][] edges, int k) {
        List<List<int[]>> graph = new ArrayList<>();
        for (int i = 0; i <= n; i++) {
            graph.add(new ArrayList<>());
        }
        for (int[] edge : edges) {
            graph.get(edge[0]).add(new int[]{edge[1], edge[2]});
            graph.get(edge[1]).add(new int[]{edge[0], edge[2]});
        }

        boolean[] infected = new boolean[n + 1];
        infected[infection] = true;

        dfs(0, k, n, infected, graph);

        return maxInfected;
    }

    private void dfs(int step, int k, int n, boolean[] infected, List<List<int[]>> graph) {
        int count = 0;
        for (boolean b : infected) {
            if (b) count++;
        }
        maxInfected = Math.max(maxInfected, count);

        if (step == k) return;

        for (int type = 1; type <= 3; type++) {
            boolean[] nextState = bfs(n, infected, graph, type);
            dfs(step + 1, k, n, nextState, graph);
        }
    }

    private boolean[] bfs(int n, boolean[] infected, List<List<int[]>> graph, int type) {
        boolean[] nextState = infected.clone();
        Queue<Integer> queue = new LinkedList<>();

        for (int i = 1; i <= n; i++) {
            if (infected[i]) {
                queue.add(i);
            }
        }

        while (!queue.isEmpty()) {
            int curr = queue.poll();
            for (int[] edge : graph.get(curr)) {
                int to = edge[0];
                int edgeType = edge[1];
                if (edgeType == type && !nextState[to]) {
                    nextState[to] = true;
                    queue.add(to);
                }
            }
        }
        return nextState;
    }
}