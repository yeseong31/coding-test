import java.util.*;

class Solution {

    private static final int[] dx = {-1, 0, 1, 0};
    private static final int[] dy = {0, 1, 0, -1};

    public int solution(String[] maps) {
        int n = maps.length;
        int m = maps[0].length();

        int[] start = null;
        int[] lever = null;
        int[] end = null;

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                char c = maps[i].charAt(j);
                if (c == 'S') {
                    start = new int[]{i, j};
                } else if (c == 'L') {
                    lever = new int[]{i, j};
                } else if (c == 'E') {
                    end = new int[]{i, j};
                }
            }
        }

        int sToL = bfs(start, 'L', maps, n, m);
        if (sToL == -1) {
            return -1;
        }

        int lToE = bfs(lever, 'E', maps, n, m);
        if (lToE == -1) {
            return -1;
        }

        return sToL + lToE;
    }

    private int bfs(int[] start, char target, String[] maps, int n, int m) {
        Queue<int[]> q = new ArrayDeque<>();
        boolean[][] visited = new boolean[n][m];

        q.offer(new int[]{start[0], start[1], 0});
        visited[start[0]][start[1]] = true;

        while (!q.isEmpty()) {
            int[] cur = q.poll();
            int x = cur[0], y = cur[1], dist = cur[2];

            if (maps[x].charAt(y) == target) {
                return dist;
            }

            for (int i = 0; i < 4; i++) {
                int nx = x + dx[i];
                int ny = y + dy[i];

                if (nx < 0 || ny < 0 || nx >= n || ny >= m) {
                    continue;
                }
                if (visited[nx][ny] || maps[nx].charAt(ny) == 'X') {
                    continue;
                }

                visited[nx][ny] = true;
                q.offer(new int[]{nx, ny, dist + 1});
            }
        }

        return -1;
    }
}