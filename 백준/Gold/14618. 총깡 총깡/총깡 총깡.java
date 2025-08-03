import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.*;

public class Main {

    private static class Node implements Comparable<Node> {
        public final int next;
        public final int cost;

        public Node(int next, int cost) {
            this.next = next;
            this.cost = cost;
        }

        @Override
        public int compareTo(Node other) {
            return Integer.compare(this.cost, other.cost);
        }
    }

    private static int[] dijkstra(int n, int start, List<List<Node>> graph) {
        int[] dist = new int[n + 1];

        Arrays.fill(dist, Integer.MAX_VALUE);
        dist[start] = 0;

        PriorityQueue<Node> pq = new PriorityQueue<>();
        pq.offer(new Node(start, 0));

        while (!pq.isEmpty()) {
            Node current = pq.poll();
            int currentNode = current.next;
            int currentCost = current.cost;

            if (currentCost > dist[currentNode]) continue;

            for (Node connectedNode : graph.get(currentNode)) {
                int nextNode = connectedNode.next;
                int nextCost = currentCost + connectedNode.cost;

                if (nextCost < dist[nextNode]) {
                    dist[nextNode] = nextCost;
                    pq.offer(new Node(nextNode, nextCost));
                }
            }
        }

        for (int i = 0; i <= n; i++) {
            if (dist[i] == Integer.MAX_VALUE) {
                dist[i] = -1;
            }
        }

        return dist;
    }

    private static String[] solution(int n, int start, int[] a, int[] b, int[][] roads) {
        String[] answer = new String[2];

        List<List<Node>> graph = new ArrayList<>();
        for (int i = 0; i <= n; i++) {
            graph.add(new ArrayList<>());
        }

        for (int[] road : roads) {
            int from = road[0], to = road[1], cost = road[2];
            graph.get(from).add(new Node(to, cost));
            graph.get(to).add(new Node(from, cost));
        }

        int[] dist = dijkstra(n, start, graph);

        Set<Integer> aSet = new HashSet<>();
        Set<Integer> bSet = new HashSet<>();
        for (int x : a) aSet.add(x);
        for (int x : b) bSet.add(x);

        int closedNode = -1;
        int minDist = Integer.MAX_VALUE;
        boolean isA = false;

        for (int i = 1; i <= n; i++) {
            if (dist[i] == -1 || (!aSet.contains(i) && !bSet.contains(i))) continue;

            boolean isInA = aSet.contains(i);
            if (dist[i] < minDist) {
                minDist = dist[i];
                closedNode = i;
                isA = isInA;
            } else if (dist[i] == minDist && isInA && !isA) {
                closedNode = i;
                isA = true;
            }
        }

        if (closedNode == -1) {
            answer[1] = "-1";
            return answer;
        }

        answer[1] = String.valueOf(minDist);
        if (aSet.contains(closedNode)) {
            answer[0] = "A";
        } else if (bSet.contains(closedNode)) {
            answer[0] = "B";
        }

        return answer;
    }

    public static void main(String[] args) throws Exception {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringBuilder sb = new StringBuilder();

        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());

        int j = Integer.parseInt(br.readLine());
        int k = Integer.parseInt(br.readLine());

        int[] a = new int[k];
        int[] b = new int[k];

        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < k; i++) {
            a[i] = Integer.parseInt(st.nextToken());
        }

        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < k; i++) {
            b[i] = Integer.parseInt(st.nextToken());
        }

        int[][] roads = new int[m][3];
        for (int i = 0; i < m; i++) {
            st = new StringTokenizer(br.readLine());
            roads[i][0] = Integer.parseInt(st.nextToken());
            roads[i][1] = Integer.parseInt(st.nextToken());
            roads[i][2] = Integer.parseInt(st.nextToken());
        }

        String[] answer = solution(n, j, a, b, roads);

        if (!answer[1].equals("-1")) {
            sb.append(answer[0]).append('\n');
        }
        sb.append(answer[1]);

        bw.write(sb.toString());
        bw.flush();
        bw.close();
    }
}