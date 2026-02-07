import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {

    private static final int INF = 10_000_001;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());
        int[][] colors = new int[n][3];

        for (int i = 0; i < n; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            colors[i][0] = Integer.parseInt(st.nextToken());
            colors[i][1] = Integer.parseInt(st.nextToken());
            colors[i][2] = Integer.parseInt(st.nextToken());
        }

        int answer = INF;
        int[] dp = new int[3];

        for (int firstColor = 0; firstColor < 3; firstColor++) {
            Arrays.fill(dp, INF);
            dp[firstColor] = colors[0][firstColor];

            for (int i = 1; i < colors.length; i++) {
                int a = Math.min(dp[1], dp[2]) + colors[i][0];
                int b = Math.min(dp[0], dp[2]) + colors[i][1];
                int c = Math.min(dp[0], dp[1]) + colors[i][2];
                dp[0] = a;
                dp[1] = b;
                dp[2] = c;
            }

            for (int i = 0; i < 3; i++) {
                if (i != firstColor) {
                    answer = Math.min(answer, dp[i]);
                }
            }
        }

        System.out.println(answer);
    }
}