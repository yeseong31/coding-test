import java.util.*;

class Solution {

    public int solution(int[][] board) {
        int n = board.length;
        int[][] newBoard = new int[n + 2][n + 2];

        for (int[] row : newBoard) Arrays.fill(row, 1);
        for (int i = 1; i <= n; i++)
            for (int j = 1; j <= n; j++)
                newBoard[i][j] = board[i - 1][j - 1];

        int[] dx = {1, 0, -1, 0};
        int[] dy = {0, 1, 0, -1};

        int[] start = {1, 1, 1, 2};
        Set<String> visited = new HashSet<>();
        Queue<int[]> q = new ArrayDeque<>();

        String startKey = encode(start);
        visited.add(startKey);
        q.offer(new int[]{1, 1, 1, 2, 0});

        while (!q.isEmpty()) {
            int[] cur = q.poll();
            int x1 = cur[0], y1 = cur[1], x2 = cur[2], y2 = cur[3], cnt = cur[4];

            if ((x1 == n && y1 == n) || (x2 == n && y2 == n)) return cnt;

            List<int[]> next = new ArrayList<>();

            for (int i = 0; i < 4; i++) {
                int nx1 = x1 + dx[i], ny1 = y1 + dy[i];
                int nx2 = x2 + dx[i], ny2 = y2 + dy[i];
                if (newBoard[nx1][ny1] == 0 && newBoard[nx2][ny2] == 0)
                    next.add(new int[]{nx1, ny1, nx2, ny2});
            }

            for (int d : new int[]{-1, 1}) {
                if (x1 == x2) {
                    if (newBoard[x1 + d][y1] == 0 && newBoard[x2 + d][y2] == 0) {
                        next.add(new int[]{x1, y1, x1 + d, y1});
                        next.add(new int[]{x2, y2, x2 + d, y2});
                    }
                } else {
                    if (newBoard[x1][y1 + d] == 0 && newBoard[x2][y2 + d] == 0) {
                        next.add(new int[]{x1, y1, x1, y1 + d});
                        next.add(new int[]{x2, y2, x2, y2 + d});
                    }
                }
            }

            for (int[] state : next) {
                if (state[0] > state[2] || (state[0] == state[2] && state[1] > state[3])) {
                    int tmp0 = state[0], tmp1 = state[1];
                    state[0] = state[2]; state[1] = state[3];
                    state[2] = tmp0; state[3] = tmp1;
                }
                String key = encode(state);
                if (visited.add(key)) {
                    q.offer(new int[]{state[0], state[1], state[2], state[3], cnt + 1});
                }
            }
        }

        return 0;
    }

    private String encode(int[] s) {
        return s[0] + "," + s[1] + "," + s[2] + "," + s[3];
    }
}