import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {

    private static final long UPPER_BOUND = 1_000_000_000;

    private static int N;
    private static long G;
    private static int K;

    private static long[] S;
    private static long[] L;
    private static int[] O;

    private static long maxExp;
    private static long[] buffer;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        G = Long.parseLong(st.nextToken());
        K = Integer.parseInt(st.nextToken());

        S = new long[N];
        L = new long[N];
        O = new int[N];

        buffer = new long[N];
        maxExp = Long.MIN_VALUE;

        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            S[i] = Long.parseLong(st.nextToken());
            L[i] = Long.parseLong(st.nextToken());
            O[i] = Integer.parseInt(st.nextToken());
            maxExp = Math.max(maxExp, L[i]);
        }

        long answer = binarySearch();
        System.out.println(answer);
    }

    private static long binarySearch() {
        long result = 0;
        long start = 0;
        long end = maxExp + UPPER_BOUND;

        while (start <= end) {
            long mid = (start + end) / 2;

            if (isSafe(mid)) {
                result = mid;
                start = mid + 1;
            } else {
                end = mid - 1;
            }
        }

        return result;
    }

    private static boolean isSafe(long x) {
        long sum = 0;
        int cnt = 0;

        for (int i = 0; i < N; i++) {
            long v = calculateBacteria(i, x);

            if (O[i] == 0) {
                sum += v;
                if (sum > G) {
                    return false;
                }
            } else {
                buffer[cnt++] = v;
            }
        }

        Arrays.sort(buffer, 0, cnt);

        int limit = cnt - K;
        if (limit < 0) {
            limit = 0;
        }

        for (int i = 0; i < limit; i++) {
            sum += buffer[i];
            if (sum > G) {
                return false;
            }
        }

        return true;
    }

    private static long calculateBacteria(int i, long x) {
        return S[i] * Math.max(1, x - L[i]);
    }
}