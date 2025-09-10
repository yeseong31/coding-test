import java.io.*;
import java.util.StringTokenizer;

public class Solution {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringBuilder sb = new StringBuilder();

        int T = Integer.parseInt(br.readLine());

        for (int testCase = 1; testCase <= T; testCase++) {
            int n = Integer.parseInt(br.readLine());
            int m = Integer.parseInt(br.readLine());

            boolean[][] checked = new boolean[n + 1][n + 1];

            for (int i = 0; i < m; i++) {
                StringTokenizer st = new StringTokenizer(br.readLine());
                int a = Integer.parseInt(st.nextToken());
                int b = Integer.parseInt(st.nextToken());
                checked[a][b] = true;
            }

            for (int k = 1; k <= n; k++) {
                for (int i = 1; i <= n; i++) {
                    for (int j = 1; j <= n; j++) {
                        if (checked[i][k] && checked[k][j]) {
                            checked[i][j] = true;
                        }
                    }
                }
            }

            int answer = 0;

            for (int i = 1; i <= n; i++) {
                int cnt = 0;

                for (int j = 1; j <= n; j++) {
                    if (i == j) continue;
                    if (checked[i][j] || checked[j][i]) cnt++;
                }

                if (cnt == n - 1) answer++;
            }

            sb.append("#").append(testCase).append(" ").append(answer).append("\n");
        }

        bw.write(sb.toString());
        bw.flush();
        bw.close();
        br.close();
    }
}