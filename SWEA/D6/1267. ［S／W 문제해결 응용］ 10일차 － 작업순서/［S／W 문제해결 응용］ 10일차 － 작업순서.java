import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.*;

public class Solution {

    private static int[] solution(List<List<Integer>> graph, int[] edges) {
        int m = edges.length;
        int[] answer = new int[m - 1];
        int idx = 0;

        Queue<Integer> queue = new LinkedList<>();
        for (int i = 1; i < m; i++) {
            if (edges[i] == 0) {
                queue.add(i);
            }
        }

        while (!queue.isEmpty()) {
            int node = queue.poll();
            answer[idx++] = node;
            for (int next : graph.get(node)) {
                if (--edges[next] == 0) {
                    queue.add(next);
                }
            }
        }

        return answer;
    }

    public static void main(String[] args) throws Exception {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringBuilder sb = new StringBuilder();

        for (int testCase = 1; testCase <= 10; testCase++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int v = Integer.parseInt(st.nextToken());
            int e = Integer.parseInt(st.nextToken());

            List<List<Integer>> graph = new ArrayList<>();
            int[] edges = new int[v + 1];

            for (int i = 0; i <= v; i++) {
                graph.add(new ArrayList<>());
            }

            st = new StringTokenizer(br.readLine());
            for (int i = 0; i < e; i++) {
                int a = Integer.parseInt(st.nextToken());
                int b = Integer.parseInt(st.nextToken());

                graph.get(a).add(b);
                edges[b]++;
            }

            sb.append("#").append(testCase).append(" ");
            for (int x : solution(graph, edges)) {
                sb.append(x).append(" ");
            }
            sb.append("\n");
        }

        bw.write(sb.toString());
        bw.flush();
        bw.close();
    }
}