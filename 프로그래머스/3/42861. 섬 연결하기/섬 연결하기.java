import java.util.Arrays;

class Solution {

    private int[] parent;
    private int[] rank_;

    private int find(int x) {
        while (parent[x] != x) {
            parent[x] = parent[parent[x]];
            x = parent[x];
        }
        return x;
    }

    private boolean union(int a, int b) {
        int ra = find(a), rb = find(b);
        if (ra == rb) return false;

        if (rank_[ra] < rank_[rb]) {
            int tmp = ra; ra = rb; rb = tmp;
        }
        parent[rb] = ra;
        if (rank_[ra] == rank_[rb]) rank_[ra]++;
        return true;
    }

    public int solution(int n, int[][] costs) {
        Arrays.sort(costs, (x, y) -> x[2] - y[2]);

        parent = new int[n];
        rank_ = new int[n];
        for (int i = 0; i < n; i++) parent[i] = i;

        int answer = 0;
        for (int[] edge : costs) {
            int a = edge[0], b = edge[1], cost = edge[2];
            if (union(a, b)) {
                answer += cost;
            }
        }
        return answer;
    }
}