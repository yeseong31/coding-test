import java.util.Arrays;

class Solution {
    
    public int solution(int n, int[][] costs) {
        int answer = 0;
        int[] parent = new int[n];
        
        Arrays.sort(costs, (a, b) -> a[2] - b[2]);
        
        for (int index = 0; index < n; index++) {
            parent[index] = index;
        }
        
        for (int[] cost : costs) {
            if (findParent(parent, cost[0]) != findParent(parent, cost[1])) {
                unionParent(parent, cost[0], cost[1]);
                answer += cost[2];
            }
        }
        
        return answer;
    }
    
    private void unionParent(int[] parent, int nodeA, int nodeB) {
        nodeA = findParent(parent, nodeA);
        nodeB = findParent(parent, nodeB);
        
        if (nodeA < nodeB) {
            parent[nodeB] = nodeA;
        } else {
            parent[nodeA] = nodeB;
        }
    }
    
    private int findParent(int[] parent, int node) {
        if (parent[node] != node) {
            return findParent(parent, parent[node]);
        }
        
        return parent[node];
    }
}