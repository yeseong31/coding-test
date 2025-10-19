import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int T = Integer.parseInt(br.readLine());

        while (T-- > 0) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int n = Integer.parseInt(st.nextToken());
            int k = Integer.parseInt(st.nextToken());

            st = new StringTokenizer(br.readLine());
            int[] times = new int[n + 1];
            for (int i = 1; i <= n; i++) {
                times[i] = Integer.parseInt(st.nextToken());
            }

            List<List<Integer>> graph = new ArrayList<>();
            for (int i = 0; i <= n; i++) graph.add(new ArrayList<>());
            int[] indegree = new int[n + 1];

            for (int i = 0; i < k; i++) {
                st = new StringTokenizer(br.readLine());
                int x = Integer.parseInt(st.nextToken());
                int y = Integer.parseInt(st.nextToken());
                graph.get(x).add(y);
                indegree[y]++;
            }

            int w = Integer.parseInt(br.readLine());

            Queue<Integer> q = new LinkedList<>();
            int[] dp = new int[n + 1];

            for (int i = 1; i <= n; i++) {
                dp[i] = times[i];
                if (indegree[i] == 0) {
                    q.offer(i);
                }
            }

            while (!q.isEmpty()) {
                int curr = q.poll();
                for (int next : graph.get(curr)) {
                    dp[next] = Math.max(dp[next], dp[curr] + times[next]);
                    if (--indegree[next] == 0) {
                        q.offer(next);
                    }
                }
            }

            System.out.println(dp[w]);
        }
    }
}