import java.util.ArrayList;
import java.util.ArrayDeque;
import java.util.HashSet;
import java.util.List;
import java.util.Queue;
import java.util.Set;

class Solution {

    private static final int[] dx = {0, 0, 1, 0, -1};
    private static final int[] dy = {0, 1, 0, -1, 0};

    private int n;
    private int m;
    private int[][] board;

    public int[][] solution(int[][] board, int[][] commands) {
        n = board.length;
        m = board[0].length;

        this.board = new int[n][m];

        for (int i = 0; i < n; i++) {
            this.board[i] = board[i].clone();
        }

        for (int[] command : commands) {
            int target = command[0];
            int direction = command[1];
            move(target, direction);
        }

        return this.board;
    }

    private void move(int start, int direction) {
        Set<Integer> group = findGroup(start, direction);
        moveGroup(group, direction);

        while (true) {
            List<Integer> brokenApps = findBroken(direction);
            if (brokenApps.isEmpty()) {
                break;
            }

            int target = brokenApps.get(0);
            Set<Integer> nextGroup = findGroup(target, direction);
            moveGroup(nextGroup, direction);
        }
    }

    private Set<Integer> findGroup(int start, int direction) {
        Set<Integer> visited = new HashSet<>();
        Queue<Integer> queue = new ArrayDeque<>();

        visited.add(start);
        queue.offer(start);

        while (!queue.isEmpty()) {
            int current = queue.poll();

            for (int i = 0; i < n; i++) {
                for (int j = 0; j < m; j++) {
                    if (board[i][j] != current) {
                        continue;
                    }

                    int nx = (i + dx[direction] + n) % n;
                    int ny = (j + dy[direction] + m) % m;
                    int next = board[nx][ny];

                    if (next != 0 && !visited.contains(next)) {
                        visited.add(next);
                        queue.offer(next);
                    }
                }
            }
        }

        return visited;
    }

    private void moveGroup(Set<Integer> group, int direction) {
        List<Point> points = new ArrayList<>();

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                int value = board[i][j];
                if (group.contains(value)) {
                    points.add(new Point(i, j, value));
                }
            }
        }

        for (Point point : points) {
            board[point.x][point.y] = 0;
        }

        for (Point point : points) {
            int nx = (point.x + dx[direction] + n) % n;
            int ny = (point.y + dy[direction] + m) % m;
            board[nx][ny] = point.value;
        }
    }

    private List<Integer> findBroken(int direction) {
        List<Integer> result = new ArrayList<>();
        boolean[] visited = new boolean[101];

        if (direction == 1 || direction == 3) {
            for (int i = 0; i < n; i++) {
                int left = board[i][0];
                int right = board[i][m - 1];

                if (left == 0 || left != right) {
                    continue;
                }

                boolean broken = false;
                for (int j = 0; j < m; j++) {
                    if (board[i][j] != left) {
                        broken = true;
                        break;
                    }
                }
                if (broken && !visited[left]) {
                    visited[left] = true;
                    result.add(left);
                }
            }
        } else {
            for (int j = 0; j < m; j++) {
                int top = board[0][j];
                int bottom = board[n - 1][j];

                if (top == 0 || top != bottom) {
                    continue;
                }

                boolean broken = false;
                for (int i = 0; i < n; i++) {
                    if (board[i][j] != top) {
                        broken = true;
                        break;
                    }
                }
                if (broken && !visited[top]) {
                    visited[top] = true;
                    result.add(top);
                }
            }
        }

        return result;
    }

    private static class Point {
        int x;
        int y;
        int value;

        Point(int x, int y, int value) {
            this.x = x;
            this.y = y;
            this.value = value;
        }
    }
}