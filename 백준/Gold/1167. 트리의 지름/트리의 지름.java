import java.io.*;
import java.util.ArrayList;
import java.util.List;
import java.util.StringTokenizer;

public class Main {

    private static final List<List<Node>> graph = new ArrayList<>();

    private static boolean[] visited;
    private static int maxDist;
    private static int deepestNode;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringBuilder sb = new StringBuilder();

        int n = Integer.parseInt(br.readLine());
        for (int i = 0; i <= n; i++) {
            graph.add(new ArrayList<>());
        }

        for (int i = 0; i < n; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int seq = Integer.parseInt(st.nextToken());

            while (true) {
                int to = Integer.parseInt(st.nextToken());
                if (to == -1) break;
                int cost = Integer.parseInt(st.nextToken());
                graph.get(seq).add(new Node(to, cost));
            }
        }

        maxDist = Integer.MIN_VALUE;
        visited = new boolean[n + 1];
        dfs(1, 0);

        maxDist = Integer.MIN_VALUE;
        visited = new boolean[n + 1];
        dfs(deepestNode, 0);

        sb.append(maxDist);

        bw.write(sb.toString());
        bw.flush();
        bw.close();
    }

    private static void dfs(int nodeNumber, int dist) {
        if (maxDist < dist) {
            maxDist = dist;
            deepestNode = nodeNumber;
        }

        visited[nodeNumber] = true;

        for (Node next : graph.get(nodeNumber)) {
            if (!visited[next.to]) {
                dfs(next.to, dist + next.cost);
            }
        }
    }

    private static class Node {
        final int to;
        final int cost;

        Node(int to, int cost) {
            this.to = to;
            this.cost = cost;
        }
    }
}