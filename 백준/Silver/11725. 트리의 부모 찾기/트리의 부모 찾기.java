import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.ArrayList;
import java.util.List;
import java.util.StringTokenizer;

public class Main {

    private static List<List<Integer>> graph;
    private static int[] parents;
    private static boolean[] visited;

    private static void dfs(int node) {
        for (int next : graph.get(node)) {
            if (visited[next]) continue;
            parents[next] = node;
            visited[next] = true;
            dfs(next);
        }
    }

    private static int[] solution(int n) {
        parents = new int[n + 1];
        visited = new boolean[n + 1];
        visited[1] = true;

        dfs(1);

        return parents;
    }

    public static void main(String[] args) throws Exception {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringBuilder sb = new StringBuilder();

        int n = Integer.parseInt(br.readLine());

        graph = new ArrayList<>();
        for (int i = 0; i <= n; i++) {
            graph.add(new ArrayList<>());
        }

        for (int i = 0; i < n - 1; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            graph.get(a).add(b);
            graph.get(b).add(a);
        }

        int[] answer = solution(n);
        for (int i = 2; i <= n; i++) {
            sb.append(answer[i]).append("\n");
        }

        bw.write(sb.toString());
        bw.flush();
        bw.close();
    }
}