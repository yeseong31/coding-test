import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.*;

public class Main {

    private static final List<int[]> startPoints = new ArrayList<>();
    private static final int[] dx = {0, 1, 0, -1};
    private static final int[] dy = {1, 0, -1, 0};

    private static int[][] board;
    private static int m;
    private static int n;
    private static int count;

    private static int solution() {
        int answer = 0;

        Queue<int[]> q = new LinkedList<>();

        for (int[] point : startPoints) {
            int x = point[0];
            int y = point[1];

            q.add(new int[]{x, y, 0});
        }

        while (!q.isEmpty()) {
            int[] curr = q.poll();
            int x = curr[0];
            int y = curr[1];
            int c = curr[2];

            answer = Math.max(answer, c);

            for (int i = 0; i < 4; i++) {
                int nx = x + dx[i];
                int ny = y + dy[i];

                if (nx < 0 || nx >= n || ny < 0 || ny >= m || board[nx][ny] != 0) continue;

                board[nx][ny] = 1;
                q.add(new int[]{nx, ny, c + 1});
                count++;
            }
        }

        return (n * m == count) ? answer : -1;
    }

    public static void main(String[] args) throws Exception {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringBuilder sb = new StringBuilder();

        StringTokenizer st = new StringTokenizer(br.readLine());
        m = Integer.parseInt(st.nextToken());
        n = Integer.parseInt(st.nextToken());

        board = new int[n][m];

        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < m; j++) {
                board[i][j] = Integer.parseInt(st.nextToken());

                if (board[i][j] == 1) {
                    startPoints.add(new int[]{i, j});
                }
                if (board[i][j] != 0) count++;
            }
        }

        int answer = solution();
        sb.append(answer);

        bw.write(sb.toString());
        bw.flush();
        bw.close();
    }
}