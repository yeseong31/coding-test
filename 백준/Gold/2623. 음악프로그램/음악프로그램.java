import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;
import java.util.PriorityQueue;
import java.util.StringTokenizer;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());

        List<List<Integer>> graph = new ArrayList<>();
        for (int i = 0; i <= n; i++) {
            graph.add(new ArrayList<>());
        }

        List<Integer> answer = new ArrayList<>();
        int[] counts = new int[n + 1];

        for (int i = 0; i < m; i++) {
            st = new StringTokenizer(br.readLine());
            int k = Integer.parseInt(st.nextToken());
            int prev = Integer.parseInt(st.nextToken());

            for (int j = 2; j <= k; j++) {
                int curr = Integer.parseInt(st.nextToken());
                graph.get(prev).add(curr);
                counts[curr]++;
                prev = curr;
            }
        }

        PriorityQueue<Integer> q = new PriorityQueue<>();
        for (int i = 1; i <= n; i++) {
            if (counts[i] == 0) {
                q.offer(i);
            }
        }

        while (!q.isEmpty()) {
            int curr = q.poll();
            answer.add(curr);

            for (int next : graph.get(curr)) {
                counts[next]--;
                if (counts[next] == 0) {
                    q.offer(next);
                }
            }
        }

        if (answer.size() != n) {
            System.out.println(0);
            return;
        }
        for (int x : answer) {
            System.out.println(x);
        }
    }
}