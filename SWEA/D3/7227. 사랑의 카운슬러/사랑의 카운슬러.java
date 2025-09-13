import java.io.*;
import java.util.StringTokenizer;

public class Solution {

    private static int n;
    private static long answer;
    private static int[][] points;
    private static int[] groups;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringBuilder sb = new StringBuilder();

        int T = Integer.parseInt(br.readLine());

        for (int testCase = 1; testCase <= T; testCase++) {
            n = Integer.parseInt(br.readLine());

            answer = Long.MAX_VALUE;
            points = new int[n][2];
            groups = new int[n];

            for (int i = 0; i < n; i++) {
                StringTokenizer st = new StringTokenizer(br.readLine());
                points[i][0] = Integer.parseInt(st.nextToken());
                points[i][1] = Integer.parseInt(st.nextToken());
            }

            dfs(0, 0, 0);
            sb.append("#").append(testCase).append(" ").append(answer).append("\n");
        }

        bw.write(sb.toString());
        bw.flush();
        bw.close();
        br.close();
    }

    private static void dfs(int c, int cntA, int cntB) {
        if (c == n) {
            update();
            return;
        }
        if (cntA < n / 2) {
            groups[c] = 1;
            dfs(c + 1, cntA + 1, cntB);
        }
        if (cntB < n / 2) {
            groups[c] = 2;
            dfs(c + 1, cntA, cntB + 1);
        }
    }

    private static void update() {
        int dx1 = 0;
        int dy1 = 0;
        int dx2 = 0;
        int dy2 = 0;

        for (int i = 0; i < n; i++) {
            if (groups[i] == 1) {
                dx1 += points[i][0];
                dy1 += points[i][1];
            } else {
                dx2 += points[i][0];
                dy2 += points[i][1];
            }
        }

        answer = Math.min(answer, getSum(dx1, dy1, dx2, dy2));
    }

    private static long getSum(int x1, int y1, int x2, int y2) {
        int x = x2 - x1;
        int y = y2 - y1;
        return (long) x * x + (long) y * y;
    }
}