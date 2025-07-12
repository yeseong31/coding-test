import java.util.Collections;
import java.util.HashMap;
import java.util.HashSet;
import java.util.Map;
import java.util.Set;

class Solution {
    public int solution(int n, int[][] results) {
        Map<Integer, Set<Integer>> wins = new HashMap<>();
        Map<Integer, Set<Integer>> loses = new HashMap<>();
        
        for (int[] result : results) {
            int w = result[0];
            int l = result[1];
            
            wins.putIfAbsent(w, new HashSet<>());
            loses.putIfAbsent(l, new HashSet<>());
            
            wins.get(w).add(l);
            loses.get(l).add(w);
        }
        
        for (int repeat = 0; repeat < n; repeat++) {
            for (int i = 1; i <= n; i++) {
                for (int w : loses.getOrDefault(i, Collections.emptySet())) {
                    wins.putIfAbsent(w, new HashSet<>());
                    wins.putIfAbsent(i, new HashSet<>());
                    wins.get(w).addAll(wins.get(i));
                }
                for (int l : wins.getOrDefault(i, Collections.emptySet())) {
                    loses.putIfAbsent(l, new HashSet<>());
                    loses.putIfAbsent(i, new HashSet<>());
                    loses.get(l).addAll(loses.get(i));
                }
            }
        }
        
        int answer = 0;
        for (int i = 1; i <= n; i++) {
            int winCount = wins.getOrDefault(i, Collections.emptySet()).size();
            int loseCount = loses.getOrDefault(i, Collections.emptySet()).size();
            
            if (winCount + loseCount == n - 1) {
                answer++;
            }
        }
        return answer;
    }
}