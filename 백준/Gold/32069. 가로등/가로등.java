import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.ArrayDeque;
import java.util.Deque;
import java.util.HashSet;
import java.util.Set;
import java.util.StringTokenizer;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringBuilder sb = new StringBuilder();

        StringTokenizer st = new StringTokenizer(br.readLine());
        long l = Long.parseLong(st.nextToken());
        int n = Integer.parseInt(st.nextToken());
        int k = Integer.parseInt(st.nextToken());

        long[] numbers = new long[n];
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < n; i++) {
            numbers[i] = Long.parseLong(st.nextToken());
        }

        long[] answer = solution(l, k, numbers);
        for (int i = 0; i < k; i++) {
            sb.append(answer[i]).append("\n");
        }

        bw.write(sb.toString());
        bw.flush();
        bw.close();
    }

    private static long[] solution(long l, int k, long[] numbers) {
        long[] answer = new long[k];
        int seq = 0;

        Set<Long> checked = new HashSet<>();
        Deque<long[]> deque = new ArrayDeque<>();

        for (long x : numbers) {
            deque.offer(new long[]{x, 0});
            checked.add(x);
        }

        while (!deque.isEmpty() && seq < k) {
            long[] curr = deque.poll();
            long pos = curr[0];
            long dist = curr[1];

            answer[seq++] = dist;
            if (seq == k) {
                break;
            }

            long left = pos - 1;
            if (left >= 0 && !checked.contains(left)) {
                checked.add(left);
                deque.offer(new long[]{left, dist + 1});
            }

            long right = pos + 1;
            if (right <= l && !checked.contains(right)) {
                checked.add(right);
                deque.offer(new long[]{right, dist + 1});
            }
        }

        return answer;
    }
}