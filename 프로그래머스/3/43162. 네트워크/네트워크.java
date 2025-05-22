import java.util.Arrays;
import java.util.HashSet;
import java.util.Set;

class Solution {
    private int findParent(int[] parents, int x) {
        if (parents[x] != x) {
            parents[x] = findParent(parents, parents[x]);
        }
        return parents[x];
    }
    
    private void unionParent(int[] parents, int a, int b) {
        a = findParent(parents, a);
        b = findParent(parents, b);
        
        if (a < b) {
            parents[b] = a;
        } else {
            parents[a] = b;
        }
    }
    
    public int solution(int n, int[][] computers) {
        int[] parents = new int[n];
        for (int i = 0; i < n; i++) {
            parents[i] = i;
        }
        
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < i; j++) {
                if (i != j && computers[i][j] == 1) {
                    unionParent(parents, i, j);
                }
            }
        }
        
        Set<Integer> roots = new HashSet<>();
        for (int i = 0; i < n; i++) {
            roots.add(findParent(parents, i));
        }
        
        return roots.size();
    }
}