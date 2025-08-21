import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.Arrays;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class Solution {

    private static final int[] dx = {-1, 0, 1, 0};
    private static final int[] dy = {0, 1, 0, -1};

    private static int n;
    private static int[][] board;
    private static boolean[][] visited;
    private static int minDay;
    private static int maxDay;

    private static boolean isOutside(int x, int y) {
        return x < 0 || x >= n || y < 0 || y >= n;
    }

    private static void bfs(int x, int y, int day) {
        Queue<int[]> queue = new LinkedList<>();
        queue.add(new int[]{x, y});
        visited[x][y] = true;

        while (!queue.isEmpty()) {
            int[] curr = queue.poll();
            x = curr[0];
            y = curr[1];

            for (int i = 0; i < 4; i++) {
                int nx = x + dx[i];
                int ny = y + dy[i];

                if (isOutside(nx, ny)) continue;
                if (board[nx][ny] > day && !visited[nx][ny]) {
                    visited[nx][ny] = true;
                    queue.offer(new int[]{nx, ny});
                }
            }
        }
    }

    private static int solution() {
        int answer = 1;

        for (int day = minDay; day < maxDay; day++) {
            int count = 0;

            for (boolean[] row : visited) {
                Arrays.fill(row, false);
            }

            for (int i = 0; i < n; i++) {
                for (int j = 0; j < n; j++) {
                    if (board[i][j] > day && !visited[i][j]) {
                        bfs(i, j, day);
                        count++;
                    }
                }
            }

            answer = Math.max(answer, count);
        }

        return answer;
    }

    public static void main(String[] args) throws Exception {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringBuilder sb = new StringBuilder();

        int T = Integer.parseInt(br.readLine());

        for (int testCase = 1; testCase <= T; testCase++) {
            n = Integer.parseInt(br.readLine());
            board = new int[n][n];
            visited = new boolean[n][n];

            minDay = Integer.MAX_VALUE;
            maxDay = Integer.MIN_VALUE;

            for (int i = 0; i < n; i++) {
                StringTokenizer st = new StringTokenizer(br.readLine());
                for (int j = 0; j < n; j++) {
                    board[i][j] = Integer.parseInt(st.nextToken());
                    minDay = Math.min(minDay, board[i][j]);
                    maxDay = Math.max(maxDay, board[i][j]);
                }
            }

            int answer = solution();
            String message = String.format("#%d %d%n", testCase, answer);
            sb.append(message);
        }

        bw.write(sb.toString());
        bw.flush();
        bw.close();
    }
}