import java.io.*;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringBuilder sb = new StringBuilder();

        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());

        int[][] board = new int[n][m];

        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < m; j++) {
                board[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        int[][][] dp = new int[n][m][3];

        for (int j = 0; j < m; j++) {
            Arrays.fill(dp[0][j], board[0][j]);
        }

        for (int i = 1; i < n; i++) {
            for (int j = 0; j < m; j++) {
                Arrays.fill(dp[i][j], Integer.MAX_VALUE);

                if (j > 0) {
                    int fromStraight = dp[i - 1][j - 1][1];
                    int fromRight = dp[i - 1][j - 1][2];
                    dp[i][j][0] = board[i][j] + Math.min(fromStraight, fromRight);
                }

                if (j < m - 1) {
                    int fromStraight = dp[i - 1][j + 1][1];
                    int fromLeft = dp[i - 1][j + 1][0];
                    dp[i][j][2] = board[i][j] + Math.min(fromStraight, fromLeft);
                }

                int fromLeft = dp[i - 1][j][0];
                int fromRight = dp[i - 1][j][2];
                dp[i][j][1] = board[i][j] + Math.min(fromLeft, fromRight);
            }
        }

        int result = Integer.MAX_VALUE;
        for (int j = 0; j < m; j++) {
            for (int k = 0; k < 3; k++) {
                result = Math.min(result, dp[n - 1][j][k]);
            }
        }

        sb.append(result);

        bw.write(sb.toString());
        bw.flush();
        bw.close();
        br.close();
    }
}