import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    private static final int MOD = 1_000_000_007;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        
        int T = Integer.parseInt(br.readLine());
        int[] numbers = new int[T];
        int maxN = 0;

        for (int i = 0; i < T; i++) {
            numbers[i] = Integer.parseInt(br.readLine());
            maxN = Math.max(maxN, numbers[i]);
        }

        long[] dp = new long[maxN + 2];
        dp[0] = 1;

        for (int i = 1; i <= maxN + 1; i++) {
            for (int j = 0; j < i; j++) {
                dp[i] = (dp[i] + dp[j] * dp[i - 1 - j]) % MOD;
            }
        }

        for (int x : numbers) {
            System.out.println(dp[x + 1]);
        }
    }
}