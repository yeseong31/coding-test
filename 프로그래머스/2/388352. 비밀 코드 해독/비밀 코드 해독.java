import java.util.*;

class Solution {
    
    private static final List<Set<Integer>> queue = new ArrayList<>();
    private static final List<List<Integer>> result = new ArrayList<>();
    
    private static int N;
    private static int[] answer;

    private static boolean isValidCase(List<Integer> currentCase) {
        
        for (int i = 0; i < queue.size(); i++) {
            Set<Integer> q = queue.get(i);
            int ans = answer[i];
            int count = 0;
            
            for (int c : currentCase) {
                if (q.contains(c)) count++;
            }
            
            if (count != ans) {
                return false;
            }
        }
        
        return true;
    }

    private static void dfs(int x, List<Integer> currentCase) {
        if (currentCase.size() == 5) {
            if (isValidCase(currentCase)) {
                result.add(new ArrayList<>(currentCase));
            }
            return;
        }
        
        if (x <= N) {
            dfs(x + 1, currentCase);
            currentCase.add(x);
            dfs(x + 1, currentCase);
            currentCase.remove(currentCase.size() - 1);
        }
    }

    public int solution(int n, int[][] qArr, int[] ans) {
        
        N = n;
        answer = ans;
        
        for (int[] arr : qArr) {
            Set<Integer> s = new HashSet<>();
            for (int v : arr) {
                s.add(v);
            }
            queue.add(s);
        }
        
        dfs(1, new ArrayList<>());
        
        return result.size();
    }
}