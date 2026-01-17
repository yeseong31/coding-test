import java.util.Arrays;
import java.util.Comparator;

class Node {
    public final int a;
    public final int b;
    public final int c;
    
    public Node(int a, int b, int c) {
        this.a = a;
        this.b = b;
        this.c = c;
    }
}

class Solution {
    
    private static int find(int[] parents, int x) {
        if (parents[x] != x) {
            parents[x] = find(parents, parents[x]);
        }
        return parents[x];
    }
    
    private static void union(int[] parents, int a, int b) {
        a = find(parents, a);
        b = find(parents, b);
        
        if (a < b) {
            parents[b] = a;
        } else {
            parents[a] = b;
        }
    }
    
    public int solution(int n, int[][] costs) {
        
        Node[] nodes = Arrays.stream(costs)
                .map(v -> new Node(v[0], v[1], v[2]))
                .sorted(Comparator.comparingInt(v -> v.c))
                .toArray(Node[]::new);
        
        int[] parents = new int[n];
        for (int i = 0; i < n; i++) {
            parents[i] = i;
        }
        
        int answer = 0;
        for (int seq = 0; seq < nodes.length; seq++) {
            int a = nodes[seq].a;
            int b = nodes[seq].b;
            
            if (find(parents, a) != find(parents, b)) {
                union(parents, a, b);
                answer += nodes[seq].c;
            }
        }
        
        return answer;
    }
}