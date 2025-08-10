import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.*;

public class Main {

    private static int solution(int n, List<List<Integer>> graph) {
        int answer = 0;

        Queue<int[]> q = new LinkedList<>();
        boolean[] visited = new boolean[n + 1];

        q.add(new int[]{1, 0});
        visited[1] = true;

        while (!q.isEmpty()) {
            int[] node = q.poll();
            int curr = node[0];
            int step = node[1];

            if (step > 2) continue;
            answer++;

            for (int next : graph.get(curr)) {
                if (!visited[next]) {
                    visited[next] = true;
                    q.add(new int[]{next, step + 1});
                }
            }
        }

        return answer - 1;
    }

    public static void main(String[] args) throws Exception {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringBuilder sb = new StringBuilder();

        int n = Integer.parseInt(br.readLine());
        int m = Integer.parseInt(br.readLine());

        List<List<Integer>> graph = new ArrayList<>();
        for (int i = 0; i <= n; i++) {
            graph.add(new ArrayList<>());
        }
        for (int i = 0; i < m; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            graph.get(a).add(b);
            graph.get(b).add(a);
        }

        int answer = solution(n, graph);
        sb.append(answer);

        bw.write(sb.toString());
        bw.flush();
        bw.close();
    }
}