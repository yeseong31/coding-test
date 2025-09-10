import java.io.*;
import java.util.PriorityQueue;
import java.util.StringTokenizer;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringBuilder sb = new StringBuilder();

        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());

        String[] gender = br.readLine().split(" ");

        PriorityQueue<Edge> pq = new PriorityQueue<>();

        int[] parents = new int[n + 1];
        for (int i = 1; i <= n; i++) {
            parents[i] = i;
        }

        for (int i = 0; i < m; i++) {
            st = new StringTokenizer(br.readLine());

            int from = Integer.parseInt(st.nextToken());
            int to = Integer.parseInt(st.nextToken());
            int dist = Integer.parseInt(st.nextToken());

            if (!gender[from - 1].equals(gender[to - 1])) {
                pq.offer(new Edge(from, to, dist));
            }
        }

        int count = 1;
        int sumDist = 0;

        while (count < n) {
            Edge curr = pq.poll();
            if (curr == null) break;

            int from = curr.from;
            int to = curr.to;
            int dist = curr.dist;

            if (find(parents, from) != find(parents, to)) {
                union(parents, from, to);
                sumDist += dist;
                count++;
            }
        }

        for (int i = 2; i <= n; i++) {
            parents[i] = find(parents, i);
            if (parents[i - 1] != parents[i]) sumDist = -1;
        }

        sb.append(sumDist);
        bw.write(sb.toString());
        bw.flush();
        bw.close();
    }

    private static int find(int[] parents, int x) {
        if (parents[x] != x) {
            parents[x] = find(parents, parents[x]);
        }
        return parents[x];
    }

    private static void union(int[] parents, int a, int b) {
        a = find(parents, a);
        b = find(parents, b);

        if (a < b) {
            parents[b] = a;
        } else {
            parents[a] = b;
        }
    }

    private static class Edge implements Comparable<Edge> {
        final int from;
        final int to;
        final int dist;

        Edge(int from, int to, int dist) {
            this.from = from;
            this.to = to;
            this.dist = dist;
        }

        @Override
        public int compareTo(Edge o) {
            if (this.dist != o.dist) {
                return Integer.compare(this.dist, o.dist);
            }
            if (this.from != o.from) {
                return Integer.compare(this.from, o.from);
            }
            return Integer.compare(this.to, o.to);
        }
    }
}