import java.io.*;
import java.util.*;

public class Main {
    static int n;
    static double[][] points;
    static double[] dist;
    static PriorityQueue<double[]> pq = new PriorityQueue<>(
            (o1, o2) -> Double.compare(o1[1], o2[1])
    );

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer st = new StringTokenizer(br.readLine());
        double startX = Double.parseDouble(st.nextToken());
        double startY = Double.parseDouble(st.nextToken());

        st = new StringTokenizer(br.readLine());
        double endX = Double.parseDouble(st.nextToken());
        double endY = Double.parseDouble(st.nextToken());

        n = Integer.parseInt(br.readLine());

        points = new double[n + 2][2];
        dist = new double[n + 2];
        Arrays.fill(dist, Double.MAX_VALUE);

        points[0][0] = startX;
        points[0][1] = startY;
        points[n + 1][0] = endX;
        points[n + 1][1] = endY;

        for (int i = 1; i <= n; i++) {
            st = new StringTokenizer(br.readLine());
            points[i][0] = Double.parseDouble(st.nextToken());
            points[i][1] = Double.parseDouble(st.nextToken());
        }

        dijkstra();
        
        System.out.printf("%.6f\n", dist[n + 1]);
    }

    static void dijkstra() {
        dist[0] = 0;
        pq.offer(new double[]{0, 0});

        while (!pq.isEmpty()) {
            double[] cur = pq.poll();
            int idx = (int)cur[0];

            if (cur[1] > dist[idx]) continue;

            for (int i = 0; i <= n + 1; i++) {
                if (idx == i) continue;

                double time = calculateTime(idx, i);

                if (dist[i] > dist[idx] + time) {
                    dist[i] = dist[idx] + time;
                    pq.offer(new double[]{i, dist[i]});
                }
            }
        }
    }

    static double calculateTime(int from, int to) {
        double distance = getDistance(from, to);

        if (from == 0 || from == n + 1) {
            return distance / 5.0;
        } else {
            double walkTime = distance / 5.0;
            double cannonTime = 2.0 + Math.abs(distance - 50.0) / 5.0;
            return Math.min(walkTime, cannonTime);
        }
    }

    static double getDistance(int from, int to) {
        double dx = points[to][0] - points[from][0];
        double dy = points[to][1] - points[from][1];
        return Math.sqrt(dx * dx + dy * dy);
    }
}