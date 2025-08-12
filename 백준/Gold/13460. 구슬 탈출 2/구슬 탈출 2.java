import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {

    private static final int[] dx = {-1, 1, 0, 0};
    private static final int[] dy = {0, 0, -1, 1};

    private static class State {
        int rx;
        int ry;
        int bx;
        int by;
        int cnt;

        State(int rx, int ry, int bx, int by, int cnt) {
            this.rx = rx;
            this.ry = ry;
            this.bx = bx;
            this.by = by;
            this.cnt = cnt;
        }
    }

    private static int[] move(int x, int y, int d, char[][] board) {
        int count = 0;
        boolean inHole = false;

        while (true) {
            if (board[x + dx[d]][y + dy[d]] == '#') break;

            x += dx[d];
            y += dy[d];
            count++;

            if (board[x][y] == 'O') {
                inHole = true;
                break;
            }
        }

        return new int[]{x, y, count, inHole ? 1 : 0};
    }

    private static int solution(int n, int m, char[][] board) {
        int rx = 0, ry = 0, bx = 0, by = 0;

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (board[i][j] == 'R') {
                    rx = i;
                    ry = j;
                } else if (board[i][j] == 'B') {
                    bx = i;
                    by = j;
                }
            }
        }

        Queue<State> q = new LinkedList<>();
        q.add(new State(rx, ry, bx, by, 0));

        boolean[][][][] visited = new boolean[n][m][n][m];
        visited[rx][ry][bx][by] = true;

        while (!q.isEmpty()) {
            State curr = q.poll();
            
            if (curr.cnt >= 10) continue;

            for (int i = 0; i < 4; i++) {
                int[] rMove = move(curr.rx, curr.ry, i, board);
                int[] bMove = move(curr.bx, curr.by, i, board);

                if (bMove[3] == 1) continue;

                if (rMove[3] == 1) return curr.cnt + 1;

                if (rMove[0] == bMove[0] && rMove[1] == bMove[1]) {
                    if (rMove[2] > bMove[2]) {
                        rMove[0] -= dx[i];
                        rMove[1] -= dy[i];
                    } else {
                        bMove[0] -= dx[i];
                        bMove[1] -= dy[i];
                    }
                }

                if (!visited[rMove[0]][rMove[1]][bMove[0]][bMove[1]]) {
                    visited[rMove[0]][rMove[1]][bMove[0]][bMove[1]] = true;
                    q.add(new State(rMove[0], rMove[1], bMove[0], bMove[1], curr.cnt + 1));
                }
            }
        }
        
        return -1;
    }

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());

        char[][] board = new char[n][m];
        for (int i = 0; i < n; i++) board[i] = br.readLine().toCharArray();

        int answer = solution(n, m, board);
        bw.write(String.valueOf(answer));
        bw.flush();
        bw.close();
    }
}