import java.util.Arrays;

class Solution {
    public int solution(int n, int[][] computers) {
        int[] parent = generateParent(n);
        connect(parent, computers);
        
        return (int) Arrays.stream(parent).distinct().count();
    }
    
    private void connect(int[] parent, int[][] computers) {
        for (int x = 1; x < parent.length; x++) {
            for (int y = 0; y < x; y++) {
                if (computers[x][y] == 1) {
                    unionParent(parent, x, y);
                }
            }
        }
        
        for (int x = 0; x < parent.length; x++) {
            parent[x] = findParent(parent, x);
        }
    }
    
    private int findParent(int[] parent, int x) {
        if (parent[x] != x) {
            return findParent(parent, parent[x]);
        }
        return parent[x];
    }
    
    private void unionParent(int[] parent, int x, int y) {
        x = findParent(parent, x);
        y = findParent(parent, y);
        
        if (x < y) {
            parent[y] = x;
        } else {
            parent[x] = y;
        }
    }
    
    private int[] generateParent(int n) {
        int[] parent = new int[n];
        for (int index = 0; index < n; index++) {
            parent[index] = index;
        }
        return parent;
    }
}