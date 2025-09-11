import java.io.*;
import java.util.ArrayList;
import java.util.List;
import java.util.StringTokenizer;

public class Main {

    private static final List<List<Integer>> graph = new ArrayList<>();

    private static int[] town;
    private static boolean[] visited;
    private static int[][] dp;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringBuilder sb = new StringBuilder();

        int n = Integer.parseInt(br.readLine());
        town = new int[n + 1];

        for (int i = 0; i <= n; i++) {
            graph.add(new ArrayList<>());
        }

        StringTokenizer st = new StringTokenizer(br.readLine());
        for (int i = 1; i <= n; i++) {
            town[i] = Integer.parseInt(st.nextToken());
        }

        for (int i = 0; i < n - 1; i++) {
            st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            graph.get(a).add(b);
            graph.get(b).add(a);
        }

        dp = new int[n + 1][2];
        visited = new boolean[n + 1];
        visited[1] = true;

        dfs(1);
        int answer = Math.max(dp[1][0], dp[1][1]);

        sb.append(answer);
        bw.write(sb.toString());
        bw.flush();
        bw.close();
    }

    private static void dfs(int curr) {
        visited[curr] = true;
        dp[curr][0] = 0;
        dp[curr][1] = town[curr];

        for (int next : graph.get(curr)) {
            if (visited[next]) continue;
            dfs(next);

            dp[curr][0] += Math.max(dp[next][0], dp[next][1]);
            dp[curr][1] += dp[next][0];
        }
    }
}