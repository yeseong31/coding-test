import java.util.*;

class Solution {

    static final int INF = (int) 1e8;

    private static int[] intensity;
    private static List<List<int[]>> graph;
    private static boolean[] isSummit;
    private static boolean[] isGate;

    public int[] solution(int n, int[][] paths, int[] gates, int[] summits) {
        graph = new ArrayList<>();
        intensity = new int[n + 1];
        isSummit = new boolean[n + 1];
        isGate = new boolean[n + 1];

        for (int i = 0; i <= n; i++) graph.add(new ArrayList<>());
        Arrays.fill(intensity, INF);

        for (int[] path : paths) {
            graph.get(path[0]).add(new int[]{path[2], path[1]});
            graph.get(path[1]).add(new int[]{path[2], path[0]});
        }

        for (int s : summits) isSummit[s] = true;
        for (int g : gates) {
            isGate[g] = true;
            intensity[g] = 0;
        }

        PriorityQueue<int[]> pq = new PriorityQueue<>(Comparator.comparingInt(a -> a[0]));
        for (int g : gates) pq.offer(new int[]{0, g});

        while (!pq.isEmpty()) {
            int[] cur = pq.poll();
            int dist = cur[0];
            int now = cur[1];

            if (dist > intensity[now]) continue;
            if (isSummit[now]) continue;

            for (int[] next : graph.get(now)) {
                int c = next[0];
                int v = next[1];
                if (isGate[v]) continue;
                int nextCost = Math.max(intensity[now], c);
                if (nextCost < intensity[v]) {
                    intensity[v] = nextCost;
                    pq.offer(new int[]{nextCost, v});
                }
            }
        }

        Arrays.sort(summits);
        int minSummit = summits[0];
        int minIntensity = intensity[summits[0]];
        for (int i = 1; i < summits.length; i++) {
            if (intensity[summits[i]] < minIntensity) {
                minIntensity = intensity[summits[i]];
                minSummit = summits[i];
            }
        }

        return new int[]{minSummit, minIntensity};
    }
}