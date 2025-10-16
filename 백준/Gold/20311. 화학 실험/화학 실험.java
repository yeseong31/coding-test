import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.PriorityQueue;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int k = Integer.parseInt(st.nextToken());

        st = new StringTokenizer(br.readLine());
        PriorityQueue<int[]> pq = new PriorityQueue<>((a, b) -> b[1] - a[1]);

        for (int seq = 1; seq <= k; seq++) {
            int count = Integer.parseInt(st.nextToken());
            pq.offer(new int[]{seq, count});
        }

        int[] result = new int[n];
        int[] prev = null;
        int seq = 0;

        while (!pq.isEmpty()) {
            int[] curr = pq.poll();
            result[seq++] = curr[0];

            if (seq == n) break;

            curr[1]--;
            if (prev != null && prev[1] > 0) {
                pq.offer(prev);
            }

            prev = curr;
        }

        if (seq < n) {
            System.out.println(-1);
            return;
        }

        Arrays.stream(result).forEach(x -> System.out.print(x + " "));
    }
}