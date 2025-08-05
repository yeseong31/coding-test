import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.*;

public class Main {

    private static int solution(int n, int x, int y, int[][] info) {
        int[] parents = new int[n + 1];
        boolean[] visited = new boolean[n + 1];
        
        for (int[] row : info) {
            int parent = row[0];
            int child = row[1];
            parents[child] = parent;
        }

        while (x != 0) {
            visited[x] = true;
            x = parents[x];
        }

        while (!visited[y]) {
            visited[y] = true;
            y = parents[y];
        }

        return y;
    }

    public static void main(String[] args) throws Exception {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringBuilder sb = new StringBuilder();

        int T = Integer.parseInt(br.readLine());
        for (int testCase = 1; testCase <= T; testCase++) {
            int n = Integer.parseInt(br.readLine());

            int[][] info = new int[n][2];

            for (int i = 0; i < n - 1; i++) {
                StringTokenizer st = new StringTokenizer(br.readLine());
                info[i][0] = Integer.parseInt(st.nextToken());
                info[i][1] = Integer.parseInt(st.nextToken());
            }

            StringTokenizer st = new StringTokenizer(br.readLine());
            int x = Integer.parseInt(st.nextToken());
            int y = Integer.parseInt(st.nextToken());

            int answer = solution(n, x, y, info);
            sb.append(answer).append("\n");
        }

        bw.write(sb.toString());
        bw.flush();
        bw.close();
    }
}