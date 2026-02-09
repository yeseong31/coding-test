import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.StringTokenizer;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringBuilder sb = new StringBuilder();

        int n = Integer.parseInt(br.readLine());

        int[] numbers = new int[n + 1];
        int[][] dp = new int[n + 1][n + 1];

        StringTokenizer st = new StringTokenizer(br.readLine());
        for (int i = 1; i <= n; i++) {
            numbers[i] = Integer.parseInt(st.nextToken());
        }

        for (int i = 2; i < n; i++) {
            for (int j = 1; i - j > 0 && i + j <= n; j++) {
                if (numbers[i - j] == numbers[i + j]) {
                    dp[i - j][i + j] = 1;
                } else {
                    break;
                }
            }
        }

        for (int i = 2; i < n; i++) {
            if (numbers[i] != numbers[i + 1]) {
                continue;
            }
            for (int j = 1; i - j > 0 && i + j + 1 <= n; j++) {
                if (numbers[i - j] == numbers[i + j + 1]) {
                    dp[i - j][i + j + 1] = 1;
                } else {
                    break;
                }
            }
        }

        int m = Integer.parseInt(br.readLine());

        for (int i = 0; i < m; i++) {
            st = new StringTokenizer(br.readLine());
            int s = Integer.parseInt(st.nextToken());
            int e = Integer.parseInt(st.nextToken());

            if (e - s == 1) {
                sb.append(numbers[s] == numbers[e] ? 1 : 0).append("\n");
            } else if (e - s == 0) {
                sb.append(1).append("\n");
            } else {
                sb.append(dp[s][e]).append("\n");
            }
        }

        bw.write(sb.toString());
        bw.flush();
        bw.close();
        br.close();
    }
}