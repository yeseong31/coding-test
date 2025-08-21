import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.*;

public class Solution {

    private static int MAX_SIZE = 101;

    private static int solution(int start, List<Set<Integer>> graph) {
        Queue<Integer> queue = new LinkedList<>();
        queue.add(start);

        boolean[] visited = new boolean[MAX_SIZE];
        visited[start] = true;

        int answer = 0;

        while (!queue.isEmpty()) {
            int size = queue.size();
            int maxNode = 0;

            for (int i = 0; i < size; i++) {
                int node = queue.remove();
                maxNode = Math.max(maxNode, node);

                for (int next : graph.get(node)) {
                    if (!visited[next]) {
                        visited[next] = true;
                        queue.offer(next);
                    }
                }
            }

            answer = maxNode;
        }

        return answer;
    }

    public static void main(String[] args) throws Exception {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringBuilder sb = new StringBuilder();

        for (int testCase = 1; testCase <= 10; testCase++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int size = Integer.parseInt(st.nextToken());
            int start = Integer.parseInt(st.nextToken());

            List<Set<Integer>> graph = new ArrayList<>();
            for (int i = 0; i < MAX_SIZE; i++) {
                graph.add(new HashSet<>());
            }

            st = new StringTokenizer(br.readLine());
            for (int i = 0; i < size / 2; i++) {
                int from = Integer.parseInt(st.nextToken());
                int to = Integer.parseInt(st.nextToken());
                graph.get(from).add(to);
            }

            int answer = solution(start, graph);
            String message = String.format("#%d %d%n", testCase, answer);
            sb.append(message);
        }

        bw.write(sb.toString());
        bw.flush();
        bw.close();
    }
}