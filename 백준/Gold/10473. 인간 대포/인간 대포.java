import java.io.*;
import java.util.*;

public class Main {

    private static final double walkDist = 5;
    private static final double cannonDist = 50;
    private static final int cannonTime = 2;

    private static int n;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringBuilder sb = new StringBuilder();

        double x, y;

        StringTokenizer st = new StringTokenizer(br.readLine());
        x = Double.parseDouble(st.nextToken());
        y = Double.parseDouble(st.nextToken());
        Point src = new Point(x, y, 0);

        st = new StringTokenizer(br.readLine());
        x = Double.parseDouble(st.nextToken());
        y = Double.parseDouble(st.nextToken());
        Point dst = new Point(x, y, 0);

        n = Integer.parseInt(br.readLine());
        Point[] cannons = new Point[n];

        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            x = Double.parseDouble(st.nextToken());
            y = Double.parseDouble(st.nextToken());
            cannons[i] = new Point(x, y, 0);
        }

        double answer = solution(src, dst, cannons);
        sb.append(String.format("%.6f", answer));

        bw.write(sb.toString());
        bw.flush();
        bw.close();
    }

    private static double solution(Point src, Point dst, Point[] cannons) {
        int totalPoints = n + 2;
        List<List<Edge>> graph = new ArrayList<>();

        for (int i = 0; i < totalPoints; i++) {
            graph.add(new ArrayList<>());
        }

        for (int i = 0; i < n; i++) {
            double dist = calculateDist(src, cannons[i]);
            double time = dist / walkDist;
            graph.get(0).add(new Edge(i + 1, time));
        }

        double directDist = calculateDist(src, dst);
        graph.get(0).add(new Edge(n + 1, directDist / walkDist));

        for (int i = 0; i < n; i++) {
            double dist = calculateDist(cannons[i], src);
            double walkTime = dist / walkDist;
            double cannonTime = calculateCannonTime(dist);
            double minTime = Math.min(walkTime, cannonTime);
            graph.get(i + 1).add(new Edge(0, minTime));
        }

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (i != j) {
                    double dist = calculateDist(cannons[i], cannons[j]);
                    double walkTime = dist / walkDist;
                    double cannonTime = calculateCannonTime(dist);
                    double minTime = Math.min(walkTime, cannonTime);

                    graph.get(i + 1).add(new Edge(j + 1, minTime));
                }
            }
        }

        for (int i = 0; i < n; i++) {
            double dist = calculateDist(cannons[i], dst);
            double walkTime = dist / walkDist;
            double cannonTime = calculateCannonTime(dist);
            double minTime = Math.min(walkTime, cannonTime);

            graph.get(i + 1).add(new Edge(n + 1, minTime));
        }

        for (int i = 0; i < n; i++) {
            double dist = calculateDist(dst, cannons[i]);
            double time = dist / walkDist;
            graph.get(n + 1).add(new Edge(i + 1, time));
        }

        double srcToDstDist = calculateDist(dst, src);
        graph.get(n + 1).add(new Edge(0, srcToDstDist / walkDist));

        return dijkstra(graph, 0, n + 1, totalPoints);
    }

    private static double calculateCannonTime(double dist) {
        if (dist == cannonDist) {
            return cannonTime;
        }

        return cannonTime + Math.abs(dist - cannonDist) / walkDist;
    }

    private static double dijkstra(List<List<Edge>> graph, int start, int end, int totalPoints) {
        double[] dist = new double[totalPoints];
        Arrays.fill(dist, Double.MAX_VALUE);
        dist[start] = 0;

        PriorityQueue<Node> pq = new PriorityQueue<>();
        pq.offer(new Node(start, 0));

        while (!pq.isEmpty()) {
            Node current = pq.poll();
            int currentNode = current.node;
            double currentDist = current.distance;

            if (currentDist > dist[currentNode]) {
                continue;
            }

            for (Edge edge : graph.get(currentNode)) {
                int nextNode = edge.to;
                double newDist = currentDist + edge.weight;

                if (newDist < dist[nextNode]) {
                    dist[nextNode] = newDist;
                    pq.offer(new Node(nextNode, newDist));
                }
            }
        }

        return dist[end];
    }

    private static double calculateDist(Point p1, Point p2) {
        double deltaX = p2.x - p1.x;
        double deltaY = p2.y - p1.y;
        return Math.sqrt((deltaX * deltaX) + (deltaY * deltaY));
    }

    private static class Point implements Comparable<Point> {
        final double x;
        final double y;
        final double t;

        Point(double x, double y, double t) {
            this.x = x;
            this.y = y;
            this.t = t;
        }

        @Override
        public int compareTo(Point o) {
            return Double.compare(this.t, o.t);
        }
    }

    private static class Edge {
        int to;
        double weight;

        Edge(int to, double weight) {
            this.to = to;
            this.weight = weight;
        }
    }

    private static class Node implements Comparable<Node> {
        int node;
        double distance;

        Node(int node, double distance) {
            this.node = node;
            this.distance = distance;
        }

        @Override
        public int compareTo(Node other) {
            return Double.compare(this.distance, other.distance);
        }
    }
}