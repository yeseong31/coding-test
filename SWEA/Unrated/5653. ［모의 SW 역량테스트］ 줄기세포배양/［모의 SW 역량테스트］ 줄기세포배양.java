import java.io.*;
import java.util.ArrayList;
import java.util.List;
import java.util.PriorityQueue;
import java.util.StringTokenizer;

public class Solution {

    private static final List<Cell> cells = new ArrayList<>();
    private static final PriorityQueue<Cell> pq = new PriorityQueue<>();

    private static final int[] dx = {1, -1, 0, 0};
    private static final int[] dy = {0, 0, 1, -1};

    private static final int DEAD = 0;
    private static final int ACTIVE = 1;
    private static final int INACTIVE = 2;

    private static boolean[][] visited;
    private static int[] power;
    private static int[] time;
    private static int[] state;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringBuilder sb = new StringBuilder();

        int T = Integer.parseInt(br.readLine());

        for (int testCase = 1; testCase <= T; testCase++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int n = Integer.parseInt(st.nextToken());
            int m = Integer.parseInt(st.nextToken());
            int k = Integer.parseInt(st.nextToken());

            init(n, m, k);

            for (int x = 0; x < n; x++) {
                st = new StringTokenizer(br.readLine());

                for (int y = 0; y < m; y++) {
                    int t = Integer.parseInt(st.nextToken());
                    if (t != 0) {
                        cells.add(new Cell(x + k, y + k, t, t));
                        visited[x + k][y + k] = true;
                    }
                }
            }

            int answer = simulation(k);
            sb.append("#").append(testCase).append(" ").append(answer).append("\n");
        }

        bw.write(sb.toString());
        bw.flush();
        bw.close();
        br.close();
    }

    static int simulation(int k) {
        for (int t = 1; t <= k; t++) {
            while (!pq.isEmpty()) {
                Cell curr = pq.poll();
                int x = curr.x;
                int y = curr.y;

                if (!visited[x][y]) {
                    visited[x][y] = true;
                    cells.add(curr);
                }
            }

            for (Cell cell : cells) {
                if (cell.state == DEAD) continue;

                if (cell.state == ACTIVE && cell.time == t) {
                    cell.state = DEAD;
                    cell.time = 0;
                    cell.health = 0;
                    continue;
                }

                if (cell.state == INACTIVE && cell.time == t) {
                    cell.state = ACTIVE;
                    cell.time = cell.health + t;

                    for (int i = 0; i < 4; i++) {
                        int nx = cell.x + dx[i];
                        int ny = cell.y + dy[i];
                        pq.add(new Cell(nx, ny, t + 1 + cell.health, cell.health));
                    }
                }
            }
        }

        int count = 0;
        for (Cell cell : cells) {
            if (cell.state == ACTIVE || cell.state == INACTIVE) count++;
        }
        return count;
    }

    private static void init(int n, int m, int k) {
        cells.clear();
        pq.clear();
        visited = new boolean[n + 2 * k][m + 2 * k];
    }

    private static class Cell implements Comparable<Cell> {
        final int x;
        final int y;

        int time;
        int health;
        int state;

        Cell(int x, int y, int time, int health) {
            this.x = x;
            this.y = y;
            this.time = time;
            this.health = health;
            this.state = INACTIVE;
        }

        @Override
        public int compareTo(Cell o) {
            return Integer.compare(o.health, this.health);
        }
    }
}