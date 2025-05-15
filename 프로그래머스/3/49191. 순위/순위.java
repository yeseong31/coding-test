import java.util.HashMap;
import java.util.HashSet;
import java.util.Map;
import java.util.Set;

class Solution {
    public int solution(int n, int[][] results) {
        int answer = 0;
        Map<Integer, Set<Integer>> wins = new HashMap<>();
        Map<Integer, Set<Integer>> loses = new HashMap<>();
        
        for (int i = 1; i <= n; i++) {
            wins.put(i, new HashSet<>());
            loses.put(i, new HashSet<>());
        }

        for (int[] result : results) {
            int w = result[0];
            int l = result[1];
            wins.get(w).add(l);
            loses.get(l).add(w);
        }
        
        for (int x = 1; x <= n; x++) {
            for (int a : loses.get(x)) {
                wins.get(a).addAll(wins.get(x));
            }
            for (int b : wins.get(x)) {
                loses.get(b).addAll(loses.get(x));
            }
        }
        
        for (int x = 1; x <= n; x++) {
            if (wins.get(x).size() + loses.get(x).size() == n - 1) {
                answer++;
            }
        }
        
        return answer;
    }
}