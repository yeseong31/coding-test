import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

class Solution {
    
    private static final Map<Integer, List<Integer>> tree = new HashMap<>();
    
    private static boolean[] visited;
    
    public int[] solution(int[] nodes, int[][] edges) {   
        int[] answer = new int[2];
        
        for (int node : nodes) {
            tree.put(node, new ArrayList<>());
        }
        
        for (int[] edge : edges) {
            int u = edge[0];
            int v = edge[1];
            tree.get(u).add(v);
            tree.get(v).add(u);
        }
        
        visited = new boolean[1000001];
        for (int root : nodes) {
            if (!visited[root] && dfs(root, -1, false)) answer[0]++;
        }
        
        visited = new boolean[1000001];
        for (int root : nodes) {
            if (!visited[root] && dfs(root, -1, true)) answer[1]++;
        }
               
        return answer;
    }
    
    private static boolean dfs(int curr, int prev, boolean isReversed) {
        List<Integer> children = tree.get(curr);
        int count = children.size();
        
        if (prev != -1) count--;
        if (isReversed && curr % 2 == count % 2) return false;
        if (!isReversed && curr % 2 != count % 2) return false;
        
        visited[curr] = true;
        
        for (int next : children) {
            if (next != prev && !dfs(next, curr, isReversed)) {
                visited[curr] = false;
                return false;
            }
        }
        
        return true;
    }
}