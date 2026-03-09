import java.util.ArrayDeque;
import java.util.Queue;

class Solution {
    
    public int solution(int[][] rectangle, int characterX, int characterY, int itemX, int itemY) {
        int[] dx = {0, 1, 0, -1};
        int[] dy = {1, 0, -1, 0};

        int[][] board = new int[102][102];
        boolean[][] visited = new boolean[102][102];

        for (int i = 0; i < 102; i++) {
            for (int j = 0; j < 102; j++) {
                board[i][j] = -1;
            }
        }

        for (int[] r : rectangle) {
            int lx = r[0] * 2;
            int ly = r[1] * 2;
            int rx = r[2] * 2;
            int ry = r[3] * 2;

            for (int x = lx; x <= rx; x++) {
                for (int y = ly; y <= ry; y++) {
                    if (lx < x && x < rx && ly < y && y < ry) {
                        board[x][y] = 0;
                    } else if (board[x][y] != 0) {
                        board[x][y] = 1;
                    }
                }
            }
        }

        Queue<int[]> q = new ArrayDeque<>();
        q.offer(new int[]{characterX * 2, characterY * 2, 0});
        visited[characterX * 2][characterY * 2] = true;

        while (!q.isEmpty()) {
            int[] cur = q.poll();
            int x = cur[0];
            int y = cur[1];
            int d = cur[2];

            if (x == itemX * 2 && y == itemY * 2) {
                return d / 2;
            }

            for (int k = 0; k < 4; k++) {
                int nx = x + dx[k];
                int ny = y + dy[k];

                if (board[nx][ny] == 1 && !visited[nx][ny]) {
                    visited[nx][ny] = true;
                    q.offer(new int[]{nx, ny, d + 1});
                }
            }
        }

        return 0;
    }
}