import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

class Solution {
    private boolean checkOddEven(int node, Map<Integer, List<Integer>> tree, boolean[] visited, int parent) {
        List<Integer> children = tree.get(node);
        int countChildren = children.size();
        
        if (parent != -1) {
            countChildren--;
        }
        
        if (node % 2 == countChildren % 2) {
            visited[node] = true;
            
            for (int child : children) {
                if (child == parent) {
                    continue;
                }
                if (!checkOddEven(child, tree, visited, node)) {
                    visited[node] = false;
                    return false;
                }
            }
        } else {
            return false;
        }
        
        return true;
    }
    
    private boolean checkReverseOddEven(int node, Map<Integer, List<Integer>> tree, boolean[] visited, int parent) {
        List<Integer> children = tree.get(node);
        int countChildren = children.size();
        
        if (parent != -1) {
            countChildren--;
        }
        
        if (node % 2 != countChildren % 2) {
            visited[node] = true;
            
            for (int child : children) {
                if (child == parent) {
                    continue;
                }
                if (!checkReverseOddEven(child, tree, visited, node)) {
                    visited[node] = false;
                    return false;
                }
            }
        } else {
            return false;   
        }
        
        return true;
    }
    
    public int[] solution(int[] nodes, int[][] edges) {
        int[] answer = new int[] {0, 0};
        Map<Integer, List<Integer>> graph = new HashMap<>();
        
        for (int node : nodes) {
            graph.put(node, new ArrayList<>());
        }
        for (int[] edge : edges) {
            graph.get(edge[0]).add(edge[1]);
            graph.get(edge[1]).add(edge[0]);
        }
        
        boolean[] visited = new boolean[1000001];
        for (int root : nodes) {
            if (!visited[root] && checkOddEven(root, graph, visited, -1)) {
                answer[0]++;
            }
        }
        
        visited = new boolean[1000001];
        for (int root : nodes) {
            if (!visited[root] && checkReverseOddEven(root, graph, visited, -1)) {
                answer[1]++;
            }
        }
        
        return answer;
    }
}