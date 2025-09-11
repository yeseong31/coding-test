import java.io.*;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {

    private static int[][] cvStore;

    public static String bfs(int x, int y, int fx, int fy) {
        int n = cvStore.length;

        Queue<int[]> q = new LinkedList<>();
        boolean[] visited = new boolean[n];

        q.offer(new int[]{x, y});

        while (!q.isEmpty()) {
            int[] curr = q.poll();

            int dist = Math.abs(curr[0] - fx) + Math.abs(curr[1] - fy);
            if (dist <= 1000) return "happy";

            for (int i = 0; i < n; i++) {
                if (visited[i]) continue;

                dist = Math.abs(curr[0] - cvStore[i][0]) + Math.abs(curr[1] - cvStore[i][1]);

                if (dist <= 1000) {
                    visited[i] = true;
                    q.offer(new int[]{cvStore[i][0], cvStore[i][1]});
                }
            }
        }

        return "sad";
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringBuilder sb = new StringBuilder();

        int t = Integer.parseInt(br.readLine());

        for (int tc = 0; tc < t; tc++) {
            int n = Integer.parseInt(br.readLine());

            StringTokenizer st = new StringTokenizer(br.readLine());
            int x = Integer.parseInt(st.nextToken());
            int y = Integer.parseInt(st.nextToken());

            cvStore = new int[n][2];
            for (int i = 0; i < n; i++) {
                st = new StringTokenizer(br.readLine());
                cvStore[i][0] = Integer.parseInt(st.nextToken());
                cvStore[i][1] = Integer.parseInt(st.nextToken());
            }

            st = new StringTokenizer(br.readLine());
            int fx = Integer.parseInt(st.nextToken());
            int fy = Integer.parseInt(st.nextToken());

            String result = bfs(x, y, fx, fy);
            sb.append(result).append('\n');
        }

        bw.write(sb.toString());
        bw.flush();
        bw.close();
        br.close();
    }
}