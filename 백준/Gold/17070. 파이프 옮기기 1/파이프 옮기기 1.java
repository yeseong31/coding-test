import java.io.*;
import java.util.StringTokenizer;

public class Main {

    private static final int SIZE = 17;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringBuilder sb = new StringBuilder();

        int n = Integer.parseInt(br.readLine());
        int[][] board = new int[n][n];

        for (int i = 0; i < n; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            for (int j = 0; j < n; j++) {
                board[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        long[][][] dp = new long[SIZE][SIZE][3];
        dp[0][1][0] = 1;

        for (int i = 0; i < n; i++) {
            for (int j = 2; j < n; j++) {
                if (board[i][j] == 1) continue;

                dp[i][j][0] += dp[i][j - 1][0] + dp[i][j - 1][1];

                if (i > 0) {
                    dp[i][j][2] += dp[i - 1][j][1] + dp[i - 1][j][2];
                }
                if (i > 0 && board[i - 1][j] == 0 && board[i][j - 1] == 0) {
                    dp[i][j][1] += dp[i - 1][j - 1][0] + dp[i - 1][j - 1][1] + dp[i - 1][j - 1][2];
                }
            }
        }

        long answer = dp[n - 1][n - 1][0] + dp[n - 1][n - 1][1] + dp[n - 1][n - 1][2];
        sb.append(answer);

        bw.write(sb.toString());
        bw.flush();
        bw.close();
    }
}