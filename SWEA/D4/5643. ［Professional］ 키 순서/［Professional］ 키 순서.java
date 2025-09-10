import java.io.*;
import java.util.ArrayList;
import java.util.List;
import java.util.StringTokenizer;

public class Solution {

    private static boolean[] visited;
    private static int count;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringBuilder sb = new StringBuilder();

        int T = Integer.parseInt(br.readLine());

        for (int testCase = 1; testCase <= T; testCase++) {
            int n = Integer.parseInt(br.readLine());
            int m = Integer.parseInt(br.readLine());

            List<List<Integer>> adj = new ArrayList<>();
            List<List<Integer>> rev = new ArrayList<>();

            for (int i = 0; i <= n; i++) {
                adj.add(new ArrayList<>());
                rev.add(new ArrayList<>());
            }

            for (int i = 0; i < m; i++) {
                StringTokenizer st = new StringTokenizer(br.readLine());
                int a = Integer.parseInt(st.nextToken());
                int b = Integer.parseInt(st.nextToken());
                adj.get(a).add(b);
                rev.get(b).add(a);
            }

            int answer = 0;

            for (int i = 1; i <= n; i++) {
                visited = new boolean[n + 1];
                count = 0;
                dfs(i, adj);  // i보다 큰 학생들 탐색
                int taller = count;

                visited = new boolean[n + 1];
                count = 0;
                dfs(i, rev);  // i보다 작은 학생들 탐색
                int shorter = count;

                if (taller + shorter == n - 1) answer++;
            }

            sb.append("#").append(testCase).append(" ").append(answer).append("\n");
        }

        bw.write(sb.toString());
        bw.flush();
        bw.close();
        br.close();
    }

    static void dfs(int current, List<List<Integer>> graph) {
        visited[current] = true;

        for (int next : graph.get(current)) {
            if (!visited[next]) {
                count++;
                dfs(next, graph);
            }
        }
    }
}
