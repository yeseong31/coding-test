import java.io.*;
import java.util.*;

public class Main {

    private static final int[] dx = {-1, 0, 1, 0};
    private static final int[] dy = {0, 1, 0, -1};

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

        int answer = solution(n, m, board);

        sb.append(answer);
        bw.write(sb.toString());
        bw.flush();
        bw.close();
    }

    private static int solution(int n, int m, int[][] board) {
        boolean[][] checked = new boolean[n][m];
        Queue<int[]> queue = new LinkedList<>();
        queue.offer(new int[]{0, 0});
        checked[0][0] = true;

        // 초기 외부 공기 표시
        while (!queue.isEmpty()) {
            int[] curr = queue.poll();
            int x = curr[0];
            int y = curr[1];

            for (int i = 0; i < 4; i++) {
                int nx = x + dx[i];
                int ny = y + dy[i];
                if (isInside(nx, ny, n, m) && !checked[nx][ny] && board[nx][ny] == 0) {
                    checked[nx][ny] = true;
                    queue.offer(new int[]{nx, ny});
                }
            }
        }

        int time = 0;

        while (true) {
            List<int[]> melts = new ArrayList<>();

            for (int x = 0; x < n; x++) {
                for (int y = 0; y < m; y++) {
                    if (board[x][y] == 1 && checkOutside(x, y, n, m, checked) >= 2) {
                        melts.add(new int[]{x, y});
                    }
                }
            }

            if (melts.isEmpty()) break;

            for (int[] c : melts) {
                int x = c[0], y = c[1];
                board[x][y] = 0;
            }

            for (int[] c : melts) {
                int x = c[0], y = c[1];
                if (!checked[x][y] && checkOutside(x, y, n, m, checked) > 0) {
                    bfs(x, y, board, checked);
                }
            }

            time++;
        }

        return time;
    }

    private static int checkOutside(int x, int y, int n, int m, boolean[][] checked) {
        int cnt = 0;
        for (int i = 0; i < 4; i++) {
            int nx = x + dx[i];
            int ny = y + dy[i];
            if (isInside(nx, ny, n, m) && checked[nx][ny]) cnt++;
        }
        return cnt;
    }

    private static void bfs(int x, int y, int[][] board, boolean[][] isOutside) {
        int n = isOutside.length;
        int m = isOutside[0].length;
        Queue<int[]> queue = new LinkedList<>();
        queue.offer(new int[]{x, y});
        isOutside[x][y] = true;

        while (!queue.isEmpty()) {
            int[] curr = queue.poll();
            int cx = curr[0];
            int cy = curr[1];

            for (int i = 0; i < 4; i++) {
                int nx = cx + dx[i];
                int ny = cy + dy[i];

                if (isInside(nx, ny, n, m) && !isOutside[nx][ny] && board[nx][ny] == 0) {
                    isOutside[nx][ny] = true;
                    queue.offer(new int[]{nx, ny});
                }
            }
        }
    }

    private static boolean isInside(int x, int y, int n, int m) {
        return x >= 0 && x < n && y >= 0 && y < m;
    }
}