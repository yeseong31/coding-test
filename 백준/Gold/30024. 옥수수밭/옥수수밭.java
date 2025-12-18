import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.PriorityQueue;
import java.util.StringTokenizer;

public class Main {

    private static final int[] dx = {-1, 0, 1, 0};
    private static final int[] dy = {0, -1, 0, 1};

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringBuilder sb = new StringBuilder();

        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());

        int[][] cornValues = new int[n][m];
        for (int x = 0; x < n; x++) {
            st = new StringTokenizer(br.readLine());
            for (int y = 0; y < m; y++) {
                cornValues[x][y] = Integer.parseInt(st.nextToken());
            }
        }

        int k = Integer.parseInt(br.readLine());

        int[][] answer = solution(n, m, k, cornValues);
        for (int i = 0; i < k; i++) {
            sb.append(answer[i][0]).append(" ").append(answer[i][1]).append("\n");
        }

        bw.write(sb.toString());
        bw.flush();
        bw.close();
    }

    private static int[][] solution(int n, int m, int k, int[][] cornValues) {
        int[][] answer = new int[k][2];
        int seq = 0;      // 지금까지 캔 옥수수의 개수

        PriorityQueue<Corn> pq = new PriorityQueue<>();
        boolean[][] visited = new boolean[n][m];

        for (int x = 0; x < n; x++) {
            for (int y = 0; y < m; y++) {
                if (x == 0 || y == 0 || x == n - 1 || y == m - 1) {
                    pq.offer(new Corn(x, y, cornValues[x][y]));
                    visited[x][y] = true;
                }
            }
        }

        while (!pq.isEmpty() && seq < k) {
            Corn corn = pq.poll();

            answer[seq][0] = corn.x + 1;
            answer[seq][1] = corn.y + 1;
            seq++;

            for (int i = 0; i < 4; i++) {
                int nx = corn.x + dx[i];
                int ny = corn.y + dy[i];

                if (0 <= nx && nx < n && 0 <= ny && ny < m && !visited[nx][ny]) {
                    pq.offer(new Corn(nx, ny, cornValues[nx][ny]));
                    visited[nx][ny] = true;
                }
            }
        }

        return answer;
    }

    private static class Corn implements Comparable<Corn> {
        final int x;
        final int y;
        final int v;

        public Corn(int x, int y, int v) {
            this.x = x;
            this.y = y;
            this.v = v;
        }

        @Override
        public int compareTo(Corn o) {
            return Integer.compare(o.v, v);
        }
    }
}