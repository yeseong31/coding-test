import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashMap;
import java.util.Map;
import java.util.StringTokenizer;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        long T = Long.parseLong(br.readLine());
        int n = Integer.parseInt(br.readLine());

        StringTokenizer st = new StringTokenizer(br.readLine());
        int[] a = new int[n];
        for (int i = 0; i < n; i++) {
            a[i] = Integer.parseInt(st.nextToken());
        }

        int m = Integer.parseInt(br.readLine());

        st = new StringTokenizer(br.readLine());
        int[] b = new int[m];
        for (int i = 0; i < m; i++) {
            b[i] = Integer.parseInt(st.nextToken());
        }

        long answer = solution(T, a, b);
        System.out.println(answer);
    }

    private static long solution(long T, int[] a, int[] b) {
        long answer = 0;

        long[] cumA = new long[a.length + 1];
        long[] cumB = new long[b.length + 1];

        for (int i = 1; i <= a.length; i++) {
            cumA[i] += cumA[i - 1] + a[i - 1];
        }
        for (int i = 1; i <= b.length; i++) {
            cumB[i] += cumB[i - 1] + b[i - 1];
        }

        Map<Long, Long> map = new HashMap<>();

        for (int left = 1; left <= a.length; left++) {
            for (int right = left; right <= a.length; right++) {
                long sum = cumA[right] - cumA[left - 1];
                map.put(sum, map.getOrDefault(sum, 0L) + 1);
            }
        }

        for (int left = 1; left <= b.length; left++) {
            for (int right = left; right <= b.length; right++) {
                long sum = cumB[right] - cumB[left - 1];
                answer += map.getOrDefault(T - sum, 0L);
            }
        }

        return answer;
    }
}