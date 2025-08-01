import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.StringTokenizer;

public class Main {

    private static int solution(int n, int d, int[][] info) {
        int[] dp = new int[d + 1];

        for (int i = 0; i <= d; i++) {
            dp[i] = i;
        }

        for (int i = 1; i <= d; i++) {
            dp[i] = Math.min(dp[i], dp[i - 1] + 1);

            for (int j = 0; j < n; j++) {
                int start = info[j][0];
                int end = info[j][1];
                int dist = info[j][2];

                if (end == i) {
                    dp[i] = Math.min(dp[i], dp[start] + dist);
                }
            }
        }

        return dp[d];
    }

    public static void main(String[] args) throws Exception {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringBuilder sb = new StringBuilder();

        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int d = Integer.parseInt(st.nextToken());

        int[][] info = new int[n][3];
        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());

            info[i][0] = Integer.parseInt(st.nextToken());
            info[i][1] = Integer.parseInt(st.nextToken());
            info[i][2] = Integer.parseInt(st.nextToken());
        }

        int answer = solution(n, d, info);
        sb.append(answer);

        bw.write(sb.toString());
        bw.flush();
        bw.close();
    }
}