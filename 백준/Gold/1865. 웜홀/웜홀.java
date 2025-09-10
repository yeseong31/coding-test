import java.io.*;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {

    private static final int INF = Integer.MAX_VALUE;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringBuilder sb = new StringBuilder();

        int TC = Integer.parseInt(br.readLine());

        while (TC-- > 0) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int n = Integer.parseInt(st.nextToken());
            int m = Integer.parseInt(st.nextToken());
            int w = Integer.parseInt(st.nextToken());

            Edge[] edges = new Edge[m * 2 + w + n];
            int seq = 0;

            for (int i = 0; i < m; i++) {
                st = new StringTokenizer(br.readLine());
                int from = Integer.parseInt(st.nextToken());
                int to = Integer.parseInt(st.nextToken());
                int dist = Integer.parseInt(st.nextToken());
                edges[seq++] = new Edge(from, to, dist);
                edges[seq++] = new Edge(to, from, dist);
            }

            for (int i = 0; i < w; i++) {
                st = new StringTokenizer(br.readLine());
                int from = Integer.parseInt(st.nextToken());
                int to = Integer.parseInt(st.nextToken());
                int time = Integer.parseInt(st.nextToken());
                edges[seq++] = new Edge(from, to, -time);
            }

            for (int i = 1; i <= n; i++) {
                edges[seq++] = new Edge(0, i, 0);
            }

            int[] distance = new int[n + 1];
            Arrays.fill(distance, INF);
            distance[0] = 0;

            boolean hasNegativeCycle = false;

            for (int i = 0; i < n; i++) {
                for (Edge edge : edges) {
                    int from = edge.from;
                    int to = edge.to;
                    int cost = edge.dist;

                    if (distance[from] != INF && distance[to] > distance[from] + cost) {
                        distance[to] = distance[from] + cost;
                    }
                }
            }

            for (Edge edge : edges) {
                int from = edge.from;
                int to = edge.to;
                int cost = edge.dist;

                if (distance[from] != INF && distance[to] > distance[from] + cost) {
                    hasNegativeCycle = true;
                    break;
                }
            }

            sb.append(hasNegativeCycle ? "YES\n" : "NO\n");
        }

        bw.write(sb.toString());
        bw.flush();
        bw.close();
    }

    private static class Edge {
        int from, to, dist;

        public Edge(int from, int to, int dist) {
            this.from = from;
            this.to = to;
            this.dist = dist;
        }
    }
}