import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int k = Integer.parseInt(st.nextToken());

        long[] a = new long[n];
        long[] b = new long[n];
        long sumA = 0;
        long sumB = 0;

        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < n; i++) {
            a[i] = Long.parseLong(st.nextToken());
            sumA += a[i];
        }

        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < n; i++) {
            b[i] = Long.parseLong(st.nextToken());
            sumB += b[i];
        }

        long answer = solution(n, k, a, b, sumA, sumB);
        System.out.println(answer);
    }

    private static long solution(int n, int k, long[] a, long[] b, long sumA, long sumB) {
        int topA = n - 1;
        int topB = n - 1;

        for (int i = 0; i < k; i++) {
            if (sumA >= sumB) {
                long val = a[topA];
                sumA -= val;
                topA--;
            } else {
                long val = b[topB];
                sumB -= val;
                topB--;
            }
        }

        return Math.max(sumA, sumB);
    }
}