import java.io.*;
import java.util.StringTokenizer;

public class Main {

    private static final int MOD = 1000;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringBuilder sb = new StringBuilder();

        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        long b = Long.parseLong(st.nextToken());

        long[][] A = new long[n][n];
        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < n; j++) {
                A[i][j] = Long.parseLong(st.nextToken());
            }
        }

        long[][] answer = getMatPow(A, b);

        for (long[] row : answer) {
            for (long x : row) {
                sb.append(x).append(" ");
            }
            sb.append("\n");
        }

        bw.write(sb.toString());
        bw.flush();
        bw.close();
    }

    private static long[][] getMatPow(long[][] A, long exp) {
        int n = A.length;
        long[][] result = new long[n][n];  // 단위 행렬
        long[][] base = new long[n][n];    // 초기 행렬

        for (int i = 0; i < n; i++) {
            result[i][i] = 1;
        }
        for (int i = 0; i < n; i++) {
            System.arraycopy(A[i], 0, base[i], 0, n);
        }

        while (exp > 0) {
            if (exp % 2 == 1) {
                result = matPow(result, base);
            }
            base = matPow(base, base);
            exp /= 2;
        }

        return result;
    }

    private static long[][] matPow(long[][] A, long[][] B) {
        int n = A.length;
        long[][] C = new long[n][n];

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                long sum = 0L;
                for (int k = 0; k < n; k++) {
                    sum += (A[i][k] * B[k][j]) % MOD;
                }
                C[i][j] = sum % MOD;
            }
        }

        return C;
    }
}