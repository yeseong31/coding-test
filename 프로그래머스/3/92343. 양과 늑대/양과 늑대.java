import java.util.*;

class Solution {

    private int[] info;
    private int[][] edges;
    private int answer;

    public int solution(int[] info, int[][] edges) {
        this.info = info;
        this.edges = edges;
        this.answer = 0;

        boolean[] visited = new boolean[info.length];
        visited[0] = true;

        dfs(1, 0, visited);
        return answer;
    }

    private void dfs(int sheep, int wolf, boolean[] visited) {
        if (sheep <= wolf) return;

        answer = Math.max(answer, sheep);

        for (int[] edge : edges) {
            int parent = edge[0];
            int child = edge[1];

            if (!visited[parent] || visited[child]) continue;

            visited[child] = true;
            if (info[child] == 1) dfs(sheep, wolf + 1, visited);
            else dfs(sheep + 1, wolf, visited);
            visited[child] = false;
        }
    }
}