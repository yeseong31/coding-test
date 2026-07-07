import java.util.*;

class Solution {

    private static final int[] DX = {0, 0, -1, 1};
    private static final int[] DY = {1, -1, 0, 0};
    private static final int MAX_RANGE = 101;

    public int solution(int[][] rectangle, int characterX, int characterY, int itemX, int itemY) {
        int[][] board = new int[MAX_RANGE + 1][MAX_RANGE + 1];
        for (int[] r : rectangle) {
            draw(board, r[0] * 2, r[1] * 2, r[2] * 2, r[3] * 2);
        }
        return bfs(board, characterX * 2, characterY * 2, itemX * 2, itemY * 2);
    }

    private void draw(int[][] board, int x1, int y1, int x2, int y2) {
        for (int i = x1; i <= x2; i++) {
            for (int j = y1; j <= y2; j++) {
                if (board[i][j] == 2) continue;
                board[i][j] = (i == x1 || i == x2 || j == y1 || j == y2) ? 1 : 2;
            }
        }
    }

    private int bfs(int[][] board, int startX, int startY, int targetX, int targetY) {
        int[][] dist = new int[MAX_RANGE + 1][MAX_RANGE + 1];
        for (int[] row : dist) Arrays.fill(row, -1);

        Queue<int[]> queue = new ArrayDeque<>();
        queue.offer(new int[]{startX, startY});
        dist[startX][startY] = 0;

        while (!queue.isEmpty()) {
            int[] curr = queue.poll();
            int x = curr[0], y = curr[1];

            if (x == targetX && y == targetY) return dist[x][y] / 2;

            for (int i = 0; i < 4; i++) {
                int nx = x + DX[i];
                int ny = y + DY[i];
                if (nx >= 0 && nx <= MAX_RANGE && ny >= 0 && ny <= MAX_RANGE
                        && board[nx][ny] == 1 && dist[nx][ny] == -1) {
                    dist[nx][ny] = dist[x][y] + 1;
                    queue.offer(new int[]{nx, ny});
                }
            }
        }

        return 0;
    }
}