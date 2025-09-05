import java.io.*;
import java.util.StringTokenizer;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringBuilder sb = new StringBuilder();

        int T = Integer.parseInt(br.readLine());

        for (int testCase = 1; testCase <= T; testCase++) {
            int n = Integer.parseInt(br.readLine());

            int[][] stickers = new int[2][n];
            for (int i = 0; i < 2; i++) {
                StringTokenizer st = new StringTokenizer(br.readLine());
                for (int j = 0; j < n; j++) {
                    stickers[i][j] = Integer.parseInt(st.nextToken());
                }
            }

            int answer = solution(n, stickers);
            sb.append(answer).append("\n");
        }

        bw.write(sb.toString());
        bw.flush();
        bw.close();
    }

    private static int solution(int n, int[][] stickers) {
        int[][] dp = new int[2][n];

        dp[0][0] = stickers[0][0];
        dp[1][0] = stickers[1][0];
        if (n == 1) return Math.max(dp[0][0], dp[1][0]);

        dp[0][1] = Math.max(dp[0][0], dp[1][0] + stickers[0][1]);
        dp[1][1] = Math.max(dp[1][0], dp[0][0] + stickers[1][1]);
        if (n == 2) return Math.max(dp[0][1], dp[1][1]);

        for (int j = 2; j < n; j++) {
            for (int i = 0; i < 2; i++) {
                dp[0][j] = Math.max(dp[1][j - 1], dp[1][j - 2]) + stickers[0][j];
                dp[1][j] = Math.max(dp[0][j - 1], dp[0][j - 2]) + stickers[1][j];
            }
        }

        return Math.max(dp[0][n - 1], dp[1][n - 1]);
    }
}