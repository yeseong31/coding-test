import java.util.*;

public class Solution {

    public int solution(int n, int[][] wires) {
        List<List<Integer>> graph = new ArrayList<>();
        for (int i = 0; i <= n; i++) {
            graph.add(new ArrayList<>());
        }

        for (int[] wire : wires) {
            int a = wire[0];
            int b = wire[1];
            graph.get(a).add(b);
            graph.get(b).add(a);
        }

        int answer = n;

        for (int[] wire : wires) {
            int a = wire[0];
            int b = wire[1];
            answer = Math.min(answer, Math.abs(2 * bfs(a, b, graph, n) - n));
        }

        return answer;
    }

    private int bfs(int start, int blocked, List<List<Integer>> graph, int n) {
        Queue<Integer> q = new LinkedList<>();
        boolean[] visited = new boolean[n + 1];

        q.add(start);
        visited[start] = true;
        visited[blocked] = true;

        int res = 1;
        while (!q.isEmpty()) {
            int v = q.poll();
            for (int next : graph.get(v)) {
                if (!visited[next]) {
                    visited[next] = true;
                    q.add(next);
                    res++;
                }
            }
        }
        return res;
    }
}