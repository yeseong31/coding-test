import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.ArrayDeque;
import java.util.Arrays;
import java.util.Deque;
import java.util.StringTokenizer;

public class Main {

    private static final Deque<Node> q = new ArrayDeque<>();
    private static final int[] dx = {-1, 0, 1, 0};
    private static final int[] dy = {0, -1, 0, 1};

    private static int r;
    private static int c;
    private static char[][] board;
    private static int[][] visited;

    static class Node {
        int x;
        int y;
        char type;

        Node(int x, int y, char type) {
            this.x = x;
            this.y = y;
            this.type = type;
        }
    }

    public static String bfs() {
        while (!q.isEmpty()) {
            Node cur = q.poll();
            int x = cur.x, y = cur.y;
            char z = cur.type;

            for (int i = 0; i < 4; i++) {
                int nx = x + dx[i];
                int ny = y + dy[i];

                if (nx < 0 || nx >= r || ny < 0 || ny >= c) continue;
                if (visited[nx][ny] > -1) continue;
                if (!(board[nx][ny] == '.' || board[nx][ny] == 'D')) continue;

                if (z == 'S') {
                    if (board[nx][ny] == 'D') {
                        return String.valueOf(visited[x][y] + 1);
                    }

                    visited[nx][ny] = visited[x][y] + 1;
                    q.add(new Node(nx, ny, 'S'));
                } else {
                    if (board[nx][ny] == 'D') continue;
                    board[nx][ny] = '*';
                    q.add(new Node(nx, ny, '*'));
                }
            }
        }
        return "KAKTUS";
    }

    public static void main(String[] args) throws Exception {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringBuilder sb = new StringBuilder();

        StringTokenizer st = new StringTokenizer(br.readLine());
        r = Integer.parseInt(st.nextToken());
        c = Integer.parseInt(st.nextToken());

        board = new char[r][c];
        visited = new int[r][c];
        for (int i = 0; i < r; i++) {
            Arrays.fill(visited[i], -1);
        }

        boolean foundS = false;

        for (int i = 0; i < r; i++) {
            String line = br.readLine();
            for (int j = 0; j < c; j++) {
                board[i][j] = line.charAt(j);

                if (!foundS && board[i][j] == 'S') {
                    q.add(new Node(i, j, 'S'));
                    visited[i][j] = 0;
                    foundS = true;
                }
            }
        }

        for (int i = 0; i < r; i++) {
            for (int j = 0; j < c; j++) {
                if (board[i][j] == '*') {
                    q.addFirst(new Node(i, j, '*'));
                }
            }
        }

        sb.append(bfs());

        bw.write(sb.toString());
        bw.flush();
        bw.close();
    }
}