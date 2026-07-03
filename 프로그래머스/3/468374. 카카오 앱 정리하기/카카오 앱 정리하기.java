class Solution {

    private static final int MAX_ID = 101;
    private static final int MAX_CELL = 100;

    private static final int[] dx = {0, 0, 1, 0, -1};
    private static final int[] dy = {0, 1, 0, -1, 0};

    private int n;
    private int m;
    private int[][] board;

    private int[][][] cells = new int[MAX_ID][MAX_CELL][2];
    private int[] counts = new int[MAX_ID];

    public int[][] solution(int[][] board, int[][] commands) {
        n = board.length;
        m = board[0].length;

        this.board = new int[n][m];

        for (int i = 0; i < n; i++) {
            this.board[i] = board[i].clone();
        }

        init();

        for (int[] command : commands) {
            move(command[0], command[1]);
        }

        return this.board;
    }

    private void init() {
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                int value = board[i][j];
                if (value == 0) continue;
                int index = counts[value]++;
                cells[value][index][0] = i;
                cells[value][index][1] = j;
            }
        }
    }

    private void move(int start, int direction) {
        boolean[] group = findGroup(start, direction);
        moveGroup(group, direction);

        while (true) {
            int broken = findBroken(direction);
            if (broken == 0) break;
            boolean[] nextGroup = findGroup(broken, direction);
            moveGroup(nextGroup, direction);
        }
    }

    private boolean[] findGroup(int start, int direction) {
        boolean[] visited = new boolean[MAX_ID];
        int[] queue = new int[MAX_ID];
        int front = 0, rear = 0;

        visited[start] = true;
        queue[rear++] = start;

        while (front < rear) {
            int current = queue[front++];

            for (int i = 0; i < counts[current]; i++) {
                int x = cells[current][i][0];
                int y = cells[current][i][1];

                int nx = (x + dx[direction] + n) % n;
                int ny = (y + dy[direction] + m) % m;

                int next = board[nx][ny];
                if (next != 0 && !visited[next]) {
                    visited[next] = true;
                    queue[rear++] = next;
                }
            }
        }

        return visited;
    }

    private void moveGroup(boolean[] group, int direction) {
        int[][] nextCells = new int[MAX_ID * MAX_CELL][3];
        int size = 0;

        for (int app = 1; app < MAX_ID; app++) {
            if (!group[app]) continue;

            for (int i = 0; i < counts[app]; i++) {
                int x = cells[app][i][0];
                int y = cells[app][i][1];

                board[x][y] = 0;

                int nx = (x + dx[direction] + n) % n;
                int ny = (y + dy[direction] + m) % m;

                nextCells[size][0] = nx;
                nextCells[size][1] = ny;
                nextCells[size][2] = app;
                size++;
            }
        }

        int[] indices = new int[MAX_ID];
        for (int i = 0; i < size; i++) {
            int x = nextCells[i][0];
            int y = nextCells[i][1];
            int app = nextCells[i][2];

            board[x][y] = app;

            int index = indices[app]++;
            cells[app][index][0] = x;
            cells[app][index][1] = y;
        }
    }

    private int findBroken(int direction) {
        boolean[] visited = new boolean[MAX_ID];

        if (direction == 1 || direction == 3) {
            for (int i = 0; i < n; i++) {
                int left = board[i][0];
                int right = board[i][m - 1];

                if (left == 0 || left != right || visited[left]) continue;

                visited[left] = true;

                for (int j = 1; j < m - 1; j++) {
                    if (board[i][j] != left) return left;
                }
            }
        } else {
            for (int j = 0; j < m; j++) {
                int top = board[0][j];
                int bottom = board[n - 1][j];

                if (top == 0 || top != bottom || visited[top]) continue;

                visited[top] = true;

                for (int i = 1; i < n - 1; i++) {
                    if (board[i][j] != top) return top;
                }
            }
        }

        return 0;
    }
}