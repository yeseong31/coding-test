import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;

public class Main {

    private static final int MOD = 1_000_000_007;

    private static long[][] mulMat(long[][] A, long[][] B) {
        long[][] C = new long[2][2];

        C[0][0] = ((A[0][0] * B[0][0]) % MOD + (A[0][1] * B[1][0]) % MOD) % MOD;
        C[0][1] = ((A[0][0] * B[0][1]) % MOD + (A[0][1] * B[1][1]) % MOD) % MOD;
        C[1][0] = ((A[1][0] * B[0][0]) % MOD + (A[1][1] * B[1][0]) % MOD) % MOD;
        C[1][1] = ((A[1][0] * B[0][1]) % MOD + (A[1][1] * B[1][1]) % MOD) % MOD;

        return C;
    }

    private static long[][] calculMatPow(long[][] A, long exp) {
        long[][] result = {{1, 0}, {0, 1}};
        long[][] base = {{A[0][0], A[0][1]}, {A[1][0], A[1][1]}};

        while (exp > 0) {
            if (exp % 2 == 1) {
                result = mulMat(result, base);
            }
            base = mulMat(base, base);
            exp /= 2;
        }

        return result;
    }

    private static long solution(long n) {
        if (n == 0) return 1;
        if (n == 1) return 3;

        long[][] A = {{2, 1}, {1, 0}};
        long[][] P = calculMatPow(A, n - 1);

        return (((P[0][0] * 3) % MOD) + (P[0][1] % MOD)) % MOD;
    }

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringBuilder sb = new StringBuilder();

        long n = Long.parseLong(br.readLine());
        long answer = solution(n);

        sb.append(answer);
        bw.write(sb.toString());
        bw.flush();
        bw.close();
    }
}