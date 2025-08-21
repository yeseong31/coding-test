import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.StringTokenizer;

public class Solution {

    static final int KIND_OF_DESSERT = 101;
    static final int[] dx = {1, 1, -1, -1};
    static final int[] dy = {1, -1, -1, 1};

    static int n;
    static int[][] board;
    static boolean[] desserts;
    static int startX;
    static int startY;
    static int maxCount;

    static boolean isOutside(int x, int y) {
        return x < 0 || x >= n || y < 0 || y >= n;
    }

    static void dfs(int x, int y, int d, int count) {
        if (count >= 1 && x == startX && y == startY) {
            maxCount = Math.max(maxCount, count);
            return;
        }

        for (int i = 0; i < 2; i++) {
            if (count == 0 && i == 1) continue;

            int nd = d + i;
            if (nd >= 4) continue;

            int nx = x + dx[nd];
            int ny = y + dy[nd];

            if (isOutside(nx, ny)) continue;

            int next = board[nx][ny];

            if (!desserts[next]) {
                desserts[next] = true;
                dfs(nx, ny, nd, count + 1);
                desserts[next] = false;
            }
        }
    }

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringBuilder sb = new StringBuilder();

        int T = Integer.parseInt(br.readLine());

        for (int testCase = 1; testCase <= T; testCase++) {
            n = Integer.parseInt(br.readLine());
            board = new int[n][n];
            maxCount = -1;

            for (int i = 0; i < n; i++) {
                StringTokenizer st = new StringTokenizer(br.readLine());
                for (int j = 0; j < n; j++) {
                    board[i][j] = Integer.parseInt(st.nextToken());
                }
            }

            for (int x = 0; x < n - 2; x++) {
                for (int y = 1; y < n - 1; y++) {
                    startX = x;
                    startY = y;
                    desserts = new boolean[KIND_OF_DESSERT];
                    dfs(x, y, 0, 0);
                }
            }

            String message = String.format("#%d %d%n", testCase, maxCount);
            sb.append(message);
        }

        bw.write(sb.toString());
        bw.flush();
        bw.close();
    }
}