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
        answer = Math.min(answer, paintHouse(0, colors));
        answer = Math.min(answer, paintHouse(1, colors));
        answer = Math.min(answer, paintHouse(2, colors));
        System.out.println(answer);
    }

    private static int paintHouse(int start, int[][] colors) {
        int result = INF;
        int[] dp = new int[3];

        Arrays.fill(dp, INF);
        dp[start] = colors[0][start];

        for (int i = 1; i < colors.length; i++) {
            int[] next = new int[3];
            Arrays.fill(next, INF);

            for (int j = 0; j < 3; j++) {
                if (dp[j] == INF) {
                    continue;
                }

                int l = (j + 2) % 3;
                int r = (j + 1) % 3;

                next[l] = Math.min(next[l], dp[j] + colors[i][l]);
                next[r] = Math.min(next[r], dp[j] + colors[i][r]);
            }

            dp = next;
        }

        for (int i = 0; i < 3; i++) {
            if (i != start) {
                result = Math.min(result, dp[i]);
            }
        }

        return result;
    }
}