import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.*;

public class Main {

    private static final int[] dx = {0, 1, 0, -1};
    private static final int[] dy = {1, 0, -1, 0};

    private static int n, m;
    private static int[][] board;
    private static int[][] areaIdMap;
    private static boolean[][] visited;
    private static final Map<Integer, Integer> areaSizeMap = new HashMap<>();

    private static void bfs(int x, int y, int areaId) {
        int area = 1;
        Queue<int[]> queue = new LinkedList<>();
        queue.offer(new int[]{x, y});
        visited[x][y] = true;
        areaIdMap[x][y] = areaId;

        while (!queue.isEmpty()) {
            int[] current = queue.poll();
            int cx = current[0];
            int cy = current[1];

            for (int i = 0; i < 4; i++) {
                int nx = cx + dx[i];
                int ny = cy + dy[i];

                if (0 <= nx && nx < n && 0 <= ny && ny < m && board[nx][ny] == 0 && !visited[nx][ny]) {
                    visited[nx][ny] = true;
                    queue.offer(new int[]{nx, ny});
                    areaIdMap[nx][ny] = areaId;
                    area++;
                }
            }
        }

        areaSizeMap.put(areaId, area);
    }

    private static void solution() {
        int areaId = 1;
        visited = new boolean[n][m];
        areaIdMap = new int[n][m];

        for (int i = 0; i < n; i++) {
            Arrays.fill(areaIdMap[i], -1);
        }

        for (int x = 0; x < n; x++) {
            for (int y = 0; y < m; y++) {
                if (board[x][y] == 0 && !visited[x][y]) {
                    bfs(x, y, areaId++);
                }
            }
        }

        for (int x = 0; x < n; x++) {
            for (int y = 0; y < m; y++) {
                if (board[x][y] == 0) continue;

                Set<Integer> seen = new HashSet<>();
                int sum = 1;

                for (int i = 0; i < 4; i++) {
                    int nx = x + dx[i];
                    int ny = y + dy[i];

                    if (nx < 0 || nx >= n || ny < 0 || ny >= m || board[nx][ny] != 0) continue;

                    int id = areaIdMap[nx][ny];
                    if (id != -1 && seen.add(id)) {
                        sum += areaSizeMap.get(id);
                    }
                }

                board[x][y] = sum % 10;
            }
        }
    }

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringBuilder sb = new StringBuilder();

        String[] tokens = br.readLine().trim().split(" ");
        n = Integer.parseInt(tokens[0]);
        m = Integer.parseInt(tokens[1]);

        board = new int[n][m];
        for (int x = 0; x < n; x++) {
            String line = br.readLine().trim();
            for (int y = 0; y < m; y++) {
                board[x][y] = line.charAt(y) - '0';
            }
        }

        solution();

        for (int[] row : board) {
            for (int cell : row) {
                sb.append(cell);
            }
            sb.append("\n");
        }

        bw.write(sb.toString());
        bw.flush();
        bw.close();
    }
}