import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {

    private static final int INF = 1_000_000_000;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer st = new StringTokenizer(br.readLine());
        int c = Integer.parseInt(st.nextToken());
        int n = Integer.parseInt(st.nextToken());

        int[][] city = new int[n][2];
        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            city[i][0] = Integer.parseInt(st.nextToken());
            city[i][1] = Integer.parseInt(st.nextToken());
        }

        int answer = solution(c, city);
        System.out.println(answer);
    }

    private static int solution(int c, int[][] city) {
        int maxCustomer = 0;
        for (int[] v : city) {
            maxCustomer = Math.max(maxCustomer, v[1]);
        }

        int limit = c + maxCustomer;
        int[] dp = new int[limit + 1];

        Arrays.fill(dp, INF);
        dp[0] = 0;

        for (int i = 1; i <= limit; i++) {
            for (int[] v : city) {
                if (i - v[1] >= 0) {
                    dp[i] = Math.min(dp[i], dp[i - v[1]] + v[0]);
                }
            }
        }

        int answer = INF;
        for (int i = c; i <= limit; i++) {
            answer = Math.min(answer, dp[i]);
        }
        return answer;
    }
}