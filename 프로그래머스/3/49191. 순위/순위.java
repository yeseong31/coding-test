class Solution {
    public int solution(int n, int[][] results) {
        int answer = 0;
        boolean[][] graph = new boolean[n][n];
        
        for (int[] edge : results) {
            int u = edge[0] - 1;
            int v = edge[1] - 1;
            graph[u][v] = true;
        }
        
        for (int u = 0; u < n; u++) {
            int wins = countForward(u, graph, new boolean[n]) - 1;
            int loses = countBackward(u, graph, new boolean[n]) - 1;
            
            if (wins + loses == n - 1) {
                answer++;
            }
        }
        
        return answer;
    }

    private int countForward(int u, boolean[][] graph, boolean[] visited) {
        int count = 1;
        
        for (int v = 0; v < graph[u].length; v++) {
            if (!graph[u][v] || visited[v]) {
                continue;
            }
            
            visited[v] = true;
            count += countForward(v, graph, visited);
        }
        
        return count;
    }
    
    private int countBackward(int u, boolean[][] graph, boolean[] visited) {
        int count = 1;
        
        for (int v = 0; v < graph[u].length; v++) {
            if (!graph[v][u] || visited[v]) {
                continue;
            }
            
            visited[v] = true;
            count += countBackward(v, graph, visited);
        }
        
        return count;
    }
}
