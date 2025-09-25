import java.io.*;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {

    private static int answer;
    private static int n;
    private static int m;
    private static boolean[][] visited;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringBuilder sb = new StringBuilder();

        StringTokenizer st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());

        answer = 0;
        visited = new boolean[n][m];
        for (boolean[] row : visited) Arrays.fill(row, false);

        dfs(0, 0);

        sb.append(answer);
        bw.write(sb.toString());
        bw.flush();
        bw.close();
    }

    private static void dfs(int k, int depth) {
        if (check(depth)) answer++;
        if (depth == n * m) return;

        for (int i = k; i < n * m; i++) {
            int x = i / m;
            int y = i % m;
            if (visited[x][y]) continue;
            visited[x][y] = true;
            dfs(i + 1, depth + 1);
            visited[x][y] = false;
        }
    }

    private static boolean check(int depth) {
        if (depth < 4) return true;

        for (int i = 0; i < n - 1; i++) {
            for (int j = 0; j < m - 1; j++) {
                if (visited[i][j]
                        && visited[i + 1][j]
                        && visited[i][j + 1]
                        && visited[i + 1][j + 1]) return false;
            }
        }

        return true;
    }
}