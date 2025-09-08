import java.io.*;
import java.util.Arrays;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {

    private static final int[] dx = {-1, 1, 0, 0, -2, -1, 1, 2, 2, 1, -1, -2};
    private static final int[] dy = {0, 0, -1, 1, 1, 2, 2, 1, -1, -2, -2, -1};

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringBuilder sb = new StringBuilder();

        int k = Integer.parseInt(br.readLine());

        StringTokenizer st = new StringTokenizer(br.readLine());
        int w = Integer.parseInt(st.nextToken());
        int h = Integer.parseInt(st.nextToken());

        int[][] board = new int[h][w];
        for (int i = 0; i < h; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < w; j++) {
                board[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        int answer = solution(h, w, k, board);

        sb.append(answer);
        bw.write(sb.toString());
        bw.flush();
        bw.close();
    }

    private static int solution(int h, int w, int k, int[][] board) {
        int[][][] visited = new int[h][w][k + 1];
        for (int[][] layer : visited) {
            for (int[] row : layer) {
                Arrays.fill(row, Integer.MAX_VALUE);
            }
        }

        Queue<int[]> q = new LinkedList<>();
        q.add(new int[]{0, 0, k});
        visited[0][0][k] = 0;

        while (!q.isEmpty()) {
            int[] curr = q.poll();
            int x = curr[0];
            int y = curr[1];
            int horseLeft = curr[2];
            int currSteps = visited[x][y][horseLeft];

            if (x == h - 1 && y == w - 1) return currSteps;

            for (int i = 0; i < 4; i++) {
                int nx = x + dx[i];
                int ny = y + dy[i];
                if (isOutside(nx, ny, h, w) || board[nx][ny] == 1) continue;

                if (visited[nx][ny][horseLeft] > currSteps + 1) {
                    visited[nx][ny][horseLeft] = currSteps + 1;
                    q.add(new int[]{nx, ny, horseLeft});
                }
            }

            if (horseLeft == 0) continue;

            for (int i = 4; i < 12; i++) {
                int nx = x + dx[i];
                int ny = y + dy[i];
                if (isOutside(nx, ny, h, w) || board[nx][ny] == 1) continue;

                if (visited[nx][ny][horseLeft - 1] > currSteps + 1) {
                    visited[nx][ny][horseLeft - 1] = currSteps + 1;
                    q.add(new int[]{nx, ny, horseLeft - 1});
                }
            }
        }

        return -1;
    }


    private static boolean isOutside(int x, int y, int h, int w) {
        return x < 0 || x >= h || y < 0 || y >= w;
    }
}