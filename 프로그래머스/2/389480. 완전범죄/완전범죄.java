import java.util.*;

class Solution {
    private class Result {
        public int a;
        public int n;
        public int m;
        
        public Result(int a, int n, int m) {
            this.a = a;
            this.n = n;
            this.m = m;
        }
    }
    
    private final Set<String> visited = new HashSet<>();
    
    private void dfs(int[][] info, int i, int a, int b, Result result) {
        String key = i + "," + a + "," + b;
        
        if (visited.contains(key)) {
            return;
        }
        visited.add(key);

        if (a >= result.n || b >= result.m || a >= result.a) {
            return;
        }
        if (i == info.length) {
            result.a = Math.min(result.a, a);
            return;
        }

        dfs(info, i + 1, a + info[i][0], b, result);
        dfs(info, i + 1, a, b + info[i][1], result);
    }
    
    public int solution(int[][] info, int n, int m) {
        Result result = new Result(n, n, m);
        dfs(info, 0, 0, 0, result);
        
        if (result.a != n) {
            return result.a;
        }
        return -1;
    }
}