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
        int rx = 0;
        int ry = 0;
        int bx = 0;
        int by = 0;
        int cnt;

        for (int i = 1; i < n - 1; i++) {
            for (int j = 1; j < m - 1; j++) {
                if (board[i][j] == 'R') {
                    rx = i;
                    ry = j;
                } else if (board[i][j] == 'B') {
                    bx = i;
                    by = j;
                }
            }
        }

        Queue<int[]> q = new LinkedList<>();
        q.add(new int[]{rx, ry, bx, by, 0});

        boolean[][][][] visited = new boolean[n][m][n][m];
        visited[rx][ry][bx][by] = true;

        while (!q.isEmpty()) {
            int[] curr = q.poll();
            rx = curr[0];
            ry = curr[1];
            bx = curr[2];
            by = curr[3];
            cnt = curr[4];

            if (cnt >= 10) continue;

            for (int i = 0; i < 4; i++) {
                int[] rMove = move(rx, ry, i, board);
                int[] bMove = move(bx, by, i, board);

                if (bMove[3] == 1) continue;
                if (rMove[3] == 1) return cnt + 1;

                int nrx = rMove[0];
                int nry = rMove[1];
                int rCnt = rMove[2];

                int nbx = bMove[0];
                int nby = bMove[1];
                int bCnt = bMove[2];

                if (nrx == nbx && nry == nby) {
                    if (rCnt > bCnt) {
                        nrx -= dx[i];
                        nry -= dy[i];
                    } else {
                        nbx -= dx[i];
                        nby -= dy[i];
                    }
                }

                if (!visited[nrx][nry][nbx][nby]) {
                    visited[nrx][nry][nbx][nby] = true;
                    q.add(new int[]{nrx, nry, nbx, nby, cnt + 1});
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