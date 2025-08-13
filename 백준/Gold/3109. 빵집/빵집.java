import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.StringTokenizer;

public class Main {

    private static final int[] dx = {-1, 0, 1};
    private static boolean[][] board;
    private static boolean[][] visited;
    private static int r;
    private static int c;

    private static boolean dfs(int x, int y) {
        if (y == c - 1) {
            board[x][y] = false;
            return true;
        }

        boolean flag = false;

        for (int i = 0; i < 3; i++) {
            int nx = x + dx[i];
            int ny = y + 1;

            if (nx < 0 || nx >= r || visited[nx][ny]) continue;
            visited[x][y] = true;
            
            if (board[nx][ny]) {
                flag = dfs(nx, ny);
            }

            if (flag) {
                board[x][y] = false;
                return true;
            }
        }

        return false;
    }

    public static void main(String[] args) throws Exception {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringBuilder sb = new StringBuilder();

        StringTokenizer st = new StringTokenizer(br.readLine());
        r = Integer.parseInt(st.nextToken());
        c = Integer.parseInt(st.nextToken());

        board = new boolean[r][c];
        visited = new boolean[r][c];
        
        for (int i = 0; i < r; i++) {
            char[] chars = br.readLine().toCharArray();
            for (int j = 0; j < c; j++) {
                if (chars[j] == '.') {
                    board[i][j] = true;
                }
            }
        }

        int answer = 0;
        for (int i = 0; i < r; i++) {
            if (dfs(i, 0)) answer++;
        }
        sb.append(answer);

        bw.write(sb.toString());
        bw.flush();
        bw.close();
    }
}