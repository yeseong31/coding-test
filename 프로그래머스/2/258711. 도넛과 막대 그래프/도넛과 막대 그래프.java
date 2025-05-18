import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashSet;
import java.util.List;
import java.util.Set;

class Solution {
    public int[] solution(int[][] edges) {
        int n = 0;
        for (int[] edge : edges) {
            n = Math.max(n, edge[0]);
            n = Math.max(n, edge[1]);
        }
        
        int[][] edgeInfo = new int[n + 1][2];
        for (int[] row : edgeInfo) {
            Arrays.fill(row, 0);
        }
        
        List<List<Integer>> graph = new ArrayList<>();
        for (int i = 0; i < n + 1; i++) {
            graph.add(new ArrayList<>());
        }
        
        int a = 0;
        int b = 0;
        for (int[] edge : edges) {
            a = edge[0];
            b = edge[1];
            graph.get(a).add(b);
            
            edgeInfo[a][1] += 1;
            edgeInfo[b][0] += 1;
        }
        
        int root = 0;
        for (int[] row : edgeInfo) {
            if (row[0] == 0 && row[1] >= 2) {
                break;
            }
            root++;
        }
        
        int donut = 0;
        int stick = 0;
        int eight = 0;
        for (int node : graph.get(root)) {
            Set<Integer> visited = new HashSet<>();
            int x = node;
            boolean isDonut = true;
            
            while (!visited.contains(x)) {
                visited.add(x);
                
                int in = edgeInfo[x][0];
                int out = edgeInfo[x][1];
                
                if (out == 0) {
                    stick++;
                    isDonut = false;
                    break;
                }
                if (out == 2) {
                    eight++;
                    isDonut = false;
                    break;
                }
                
                x = graph.get(x).get(0);
            }
            
            if (isDonut) {
                donut++;
            }
        }
        
        return new int[] {root, donut, stick, eight};
    }
}