import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;
import java.util.StringTokenizer;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());

        List<Node> nodes = new ArrayList<>();
        for (int i = 0; i < m; i++) {
            st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            int c = Integer.parseInt(st.nextToken());
            nodes.add(new Node(a, b, c));
        }
        nodes.sort(Node::compareTo);

        int[] parents = new int[n + 1];
        for (int i = 0; i <= n; i++) {
            parents[i] = i;
        }

        int answer = 0;
        int maxC = Integer.MIN_VALUE;

        for (Node node : nodes) {
            int a = node.a;
            int b = node.b;
            int c = node.c;

            if (find(parents, a) != find(parents, b)) {
                union(parents, a, b);
                maxC = Math.max(maxC, c);
                answer += c;
            }
        }

        System.out.println(answer - maxC);
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
            parents[a] = b;
        } else {
            parents[b] = a;
        }
    }

    private static class Node implements Comparable<Node> {
        final int a;
        final int b;
        final int c;

        public Node(int a, int b, int c) {
            this.a = a;
            this.b = b;
            this.c = c;
        }

        @Override
        public int compareTo(Node o) {
            return this.c - o.c;
        }
    }
}