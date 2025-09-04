import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    private static final int INF = Integer.MAX_VALUE;
    private static List<List<Node>> graph;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());
        int x = Integer.parseInt(st.nextToken());

        graph = new ArrayList<>();
        for (int i = 0; i <= n; i++) {
            graph.add(new ArrayList<>());
        }

        for (int i = 0; i < m; i++) {
            st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            int c = Integer.parseInt(st.nextToken());
            graph.get(a).add(new Node(b, c));
        }

        int[] answer = new int[n + 1];

        for (int i = 1; i <= n; i++) {
            int[] dist = dijkstra(i, n);
            answer[i] = dist[x];
        }

        int[] fromParty = dijkstra(x, n);
        for (int i = 1; i <= n; i++) {
            answer[i] += fromParty[i];
        }

        int maxTime = 0;
        for (int i = 1; i <= n; i++) {
            maxTime = Math.max(maxTime, answer[i]);
        }

        System.out.println(maxTime);
    }

    private static int[] dijkstra(int start, int n) {
        PriorityQueue<Node> pq = new PriorityQueue<>();
        int[] distance = new int[n + 1];
        Arrays.fill(distance, INF);

        pq.offer(new Node(start, 0));
        distance[start] = 0;

        while (!pq.isEmpty()) {
            Node curr = pq.poll();
            int currNode = curr.to;
            int currCost = curr.cost;

            if (currCost > distance[currNode]) continue;

            for (Node next : graph.get(currNode)) {
                int nextNode = next.to;
                int nextCost = currCost + next.cost;

                if (nextCost < distance[nextNode]) {
                    distance[nextNode] = nextCost;
                    pq.offer(new Node(nextNode, nextCost));
                }
            }
        }

        return distance;
    }

    private static class Node implements Comparable<Node> {
        final int to;
        final int cost;

        Node(int to, int cost) {
            this.to = to;
            this.cost = cost;
        }

        @Override
        public int compareTo(Node o) {
            return Integer.compare(this.cost, o.cost);
        }
    }
}