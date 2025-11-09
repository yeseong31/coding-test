import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {

    private static final int MOD = 1_000_000_007;
    private static final int SIZE = 101;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int n = Integer.parseInt(st.nextToken());
        int k = Integer.parseInt(st.nextToken());
        int[] t = Arrays.stream(br.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();

        long answer = solution(n, k, t);
        System.out.println(answer);
    }

    private static long solution(int n, int k, int[] t) {
        long answer = 1;

        long[][] c = buildCombination();

        int s = 1;
        int e = n;
        int[] mIdx = new int[k];

        for (int i = 0; i < k; i++) {
            int m = (s + e) / 2;
            mIdx[i] = m;

            if (i == k - 1) {
                break;
            }
            if (t[i + 1] < t[i]) {
                e = m - 1;
            } else {
                s = m + 1;
            }
        }

        for (int i = 0; i < k - 1; i++) {
            for (int j = i + 1; j < k; j++) {
                if (mIdx[i] > mIdx[j]) {
                    swap(mIdx, i, j);
                    swap(t, i, j);
                }
            }
        }

        int prevPos = 0;
        int prevVal = 0;

        for (int i = 0; i < k; i++) {
            answer = answer * c[t[i] - prevVal - 1][mIdx[i] - prevPos - 1] % MOD;
            prevPos = mIdx[i];
            prevVal = t[i];
        }

        answer = answer * c[100 - prevVal][n - prevPos] % MOD;
        return answer;
    }

    private static void swap(int[] arr, int a, int b) {
        int tmp = arr[a];
        arr[a] = arr[b];
        arr[b] = tmp;
    }

    private static long[][] buildCombination() {
        long[][] c = new long[SIZE][SIZE];

        for (int n = 0; n < SIZE; n++) {
            c[n][0] = 1;
            c[n][n] = 1;
            for (int r = 1; r < n; r++) {
                c[n][r] = (c[n - 1][r - 1] + c[n - 1][r]) % MOD;
            }
        }

        return c;
    }
}