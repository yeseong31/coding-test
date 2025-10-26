import java.util.*;

public class Solution {

    private static List<List<Integer>> graph;
    private static int n;

    public int solution(int n, int[][] wires) {
        Solution.n = n;  // 클래스 필드에 저장
        graph = new ArrayList<>();
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
            answer = Math.min(answer, Math.abs(2 * bfs(a, b) - n));
        }

        return answer;
    }
    
    private static int bfs(int start, int blocked) {
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