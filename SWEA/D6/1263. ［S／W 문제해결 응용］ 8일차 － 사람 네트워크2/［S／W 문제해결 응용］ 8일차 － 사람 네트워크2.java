import java.io.*;
import java.util.StringTokenizer;

public class Solution {

    private static final int INF = 1001;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringBuilder sb = new StringBuilder();

        int T = Integer.parseInt(br.readLine());

        for (int testCase = 1; testCase <= T; testCase++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int n = Integer.parseInt(st.nextToken());

            int[][] distance = new int[n][n];

            for (int i = 0; i < n; i++) {
                for (int j = 0; j < n; j++) {
                    distance[i][j] = Integer.parseInt(st.nextToken());
                    if (i != j && distance[i][j] == 0) distance[i][j] = INF;
                }
            }

            for (int k = 0; k < n; k++) {
                for (int i = 0; i < n; i++) {
                    for (int j = 0; j < n; j++) {
                        distance[i][j] = Math.min(distance[i][j], distance[i][k] + distance[k][j]);
                    }
                }
            }

            int maxCC = Integer.MAX_VALUE;

            for (int i = 0; i < n; i++) {
                int cc = 0;
                for (int j = 0; j < n; j++) {
                    cc += distance[i][j];
                }
                maxCC = Math.min(maxCC, cc);
            }

            sb.append("#").append(testCase).append(" ").append(maxCC).append("\n");
        }

        bw.write(sb.toString());
        bw.flush();
        bw.close();
        br.close();
    }
}