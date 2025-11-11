import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int d = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());

        long[] dp = new long[d + 2];
        dp[0] = 1;
        dp[2] = 1;

        for (int i = 4; i <= d; i += 2) {
            long sum = dp[i - 2];
            for (int j = 2; j < i; j += 2) {
                sum += dp[j] * dp[i - j - 2];
                sum %= m;
            }
            dp[i] = sum;
        }

        System.out.println(dp[d - 2] % m);
    }
}