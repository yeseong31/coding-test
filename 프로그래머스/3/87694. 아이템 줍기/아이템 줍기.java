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
                if (i > x1 && i < x2 && j > y1 && j < y2) {
                    board[i][j] = 2;
                } else {
                    board[i][j] = 1;
                }
            }
        }
    }

    private int bfs(int[][] board, int startX, int startY, int targetX, int targetY) {
        Queue<int[]> queue = new ArrayDeque<>();
        boolean[][] visited = new boolean[MAX_RANGE + 1][MAX_RANGE + 1];

        queue.offer(new int[]{startX, startY, 0});
        visited[startX][startY] = true;

        while (!queue.isEmpty()) {
            int[] curr = queue.poll();
            
            if (curr[0] == targetX && curr[1] == targetY) {
                return curr[2] / 2;
            }

            for (int i = 0; i < 4; i++) {
                int nx = curr[0] + DX[i];
                int ny = curr[1] + DY[i];

                if (isValid(nx, ny) && board[nx][ny] == 1 && !visited[nx][ny]) {
                    visited[nx][ny] = true;
                    queue.offer(new int[]{nx, ny, curr[2] + 1});
                }
            }
        }
        return 0;
    }

    private boolean isValid(int x, int y) {
        return x >= 0 && x <= MAX_RANGE && y >= 0 && y <= MAX_RANGE;
    }
}