import java.util.*;

class Solution {
    
    private static final List<List<Integer>> graph = new ArrayList<>();;
    
    private static int[][] dp;
    private static boolean[] visited;

    public int solution(int n, int[][] lighthouse) {
        for (int i = 0; i <= n; i++) {
            graph.add(new ArrayList<>());
        }

        for (int[] edge : lighthouse) {
            graph.get(edge[0]).add(edge[1]);
            graph.get(edge[1]).add(edge[0]);
        }

        dp = new int[n + 1][2];
        visited = new boolean[n + 1];

        dfs(1);
        
        return Math.min(dp[1][0], dp[1][1]);
    }

    private void dfs(int node) {
        visited[node] = true;
        dp[node][0] = 0;
        dp[node][1] = 1;

        for (int child : graph.get(node)) {
            if (visited[child]) continue;
            
            dfs(child);

            dp[node][0] += dp[child][1];
            dp[node][1] += Math.min(dp[child][0], dp[child][1]);
        }
    }
}