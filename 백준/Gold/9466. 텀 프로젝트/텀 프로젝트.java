import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int T = Integer.parseInt(br.readLine());

        for (int i = 0; i < T; i++) {
            int n = Integer.parseInt(br.readLine());

            StringTokenizer st = new StringTokenizer(br.readLine());
            int[] numbers = new int[n];
            for (int j = 0; j < n; j++) {
                numbers[j] = Integer.parseInt(st.nextToken());
            }

            System.out.println(solution(n, numbers));
        }
    }

    private static int solution(int n, int[] numbers) {
        List<List<Integer>> graph = new ArrayList<>();
        int[] indegrees = new int[n + 1];

        for (int i = 0; i <= n; i++) {
            graph.add(new ArrayList<>());
        }

        for (int i = 1; i <= n; i++) {
            graph.get(i).add(numbers[i - 1]);
            ++indegrees[numbers[i - 1]];
        }

        Queue<Integer> q = new LinkedList<>();
        for (int i = 1; i <= n; i++) {
            if (indegrees[i] == 0) {
                q.add(i);
            }
        }

        int removed = 0;
        while (!q.isEmpty()) {
            int curr = q.poll();
            removed++;

            for (int next : graph.get(curr)) {
                if (--indegrees[next] == 0) {
                    q.add(next);
                }
            }
        }

        return removed;
    }
}