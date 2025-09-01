import java.io.*;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {

    private static final int SIZE = 101;
    private static final int MID = 50;
    private static final int[][][] dp = new int[SIZE][SIZE][SIZE];

    private static int w(int a, int b, int c) {
        if (dp[a + MID][b + MID][c + MID] < Integer.MAX_VALUE) {
            return dp[a + MID][b + MID][c + MID];
        }

        if (a <= 0 || b <= 0 || c <= 0) {
            dp[a + MID][b + MID][c + MID] = 1;
            return 1;
        }

        if (a > 20 || b > 20 || c > 20) {
            dp[a + MID][b + MID][c + MID] = w(20, 20, 20);
        } else if (a < b && b < c) {
            dp[a + MID][b + MID][c + MID] = w(a, b, c - 1) + w(a, b - 1, c - 1) - w(a, b - 1, c);
        } else {
            dp[a + MID][b + MID][c + MID] = w(a - 1, b, c) + w(a - 1, b - 1, c) + w(a - 1, b, c - 1) - w(a - 1, b - 1, c - 1);
        }

        return dp[a + MID][b + MID][c + MID];
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringBuilder sb = new StringBuilder();

        for (int i = 0; i < SIZE; i++) {
            for (int j = 0; j < SIZE; j++) {
                Arrays.fill(dp[i][j], Integer.MAX_VALUE);
            }
        }

        while (true) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            int c = Integer.parseInt(st.nextToken());

            if (a == -1 && b == -1 && c == -1) break;

            w(a, b, c);

            sb.append("w(")
                    .append(a)
                    .append(", ")
                    .append(b)
                    .append(", ")
                    .append(c)
                    .append(") = ")
                    .append(dp[a + MID][b + MID][c + MID])
                    .append("\n");
        }

        bw.write(sb.toString());
        bw.flush();
        bw.close();
    }
}