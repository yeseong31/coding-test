import java.util.*;

class Solution {
    
    static final int INF = (int) 1e8;

    static class Node implements Comparable<Node> {
        int cost;
        int to;

        Node(int cost, int to) {
            this.cost = cost;
            this.to = to;
        }

        @Override
        public int compareTo(Node o) {
            return Integer.compare(this.cost, o.cost);
        }
    }

    private void dijkstra(int start, List<List<Node>> graph, Set<Integer> summitsSet, Set<Integer> gatesSet, int[] intensity) {
        PriorityQueue<Node> pq = new PriorityQueue<>();
        intensity[start] = 0;
        pq.offer(new Node(0, start));

        while (!pq.isEmpty()) {
            Node cur = pq.poll();
            int dist = cur.cost;
            int now = cur.to;

            if (summitsSet.contains(now) || dist > intensity[now]) {
                continue;
            }

            for (Node next : graph.get(now)) {
                int c = next.cost;
                int v = next.to;

                if (gatesSet.contains(v)) {
                    continue;
                }

                int nextCost = Math.max(intensity[now], c);
                if (nextCost < intensity[v]) {
                    intensity[v] = nextCost;
                    pq.offer(new Node(nextCost, v));
                }
            }
        }
    }

    public int[] solution(int n, int[][] paths, int[] gates, int[] summits) {
        int minSummit = 0;
        int minIntensity = INF;

        List<List<Node>> graph = new ArrayList<>();
        for (int i = 0; i <= n; i++) {
            graph.add(new ArrayList<>());
        }

        for (int[] path : paths) {
            int a = path[0];
            int b = path[1];
            int c = path[2];
            graph.get(a).add(new Node(c, b));
            graph.get(b).add(new Node(c, a));
        }

        Set<Integer> summitsSet = new HashSet<>();
        for (int summit : summits) {
            summitsSet.add(summit);
        }

        Set<Integer> gatesSet = new HashSet<>();
        for (int gate : gates) {
            gatesSet.add(gate);
        }

        int[] intensity = new int[n + 1];
        Arrays.fill(intensity, INF);

        for (int gate : gates) {
            dijkstra(gate, graph, summitsSet, gatesSet, intensity);
        }

        Arrays.sort(summits);
        for (int summit : summits) {
            if (intensity[summit] < minIntensity) {
                minIntensity = intensity[summit];
                minSummit = summit;
            }
        }

        return new int[] {minSummit, minIntensity};
    }
}