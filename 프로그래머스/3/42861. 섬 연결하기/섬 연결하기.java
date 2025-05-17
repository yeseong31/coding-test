import java.util.PriorityQueue;

class Solution {
    private class Node implements Comparable<Node> {
        public int a;
        public int b;
        public int c;
        
        public Node(int a, int b, int c) {
            this.a = a;
            this.b = b;
            this.c = c;
        }
        
        @Override
        public int compareTo(Node other) {
            return this.c - other.c;
        }
    }
    
    private int findParent(int[] parents, int x) {
        if (parents[x] != x) {
            parents[x] = this.findParent(parents, parents[x]);
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
    
    public int solution(int n, int[][] costs) {
        int answer = 0;
        PriorityQueue<Node> pq = new PriorityQueue<>();
        
        for (int[] cost : costs) {
            int a = cost[0];
            int b = cost[1];
            int c = cost[2];
            
            pq.add(new Node(a, b, c));
        }
        
        int[] parents = new int[n];
        for (int i = 0; i < n; i++) {
            parents[i] = i;
        }
        
        while (!pq.isEmpty()) {
            Node node = pq.poll();
            
            if (findParent(parents, node.a) != findParent(parents, node.b)) {
                unionParent(parents, node.a, node.b);
                answer += node.c;
            }
        }

        return answer;
    }
}