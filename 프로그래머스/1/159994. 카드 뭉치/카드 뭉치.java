import java.util.*;

class Solution {
    
    public String solution(String[] cards1, String[] cards2, String[] goal) {
        Deque<String> q1 = new ArrayDeque<>(Arrays.asList(cards1));
        Deque<String> q2 = new ArrayDeque<>(Arrays.asList(cards2));
        
        for (String word : goal) {
            if (!q1.isEmpty() && q1.peekFirst().equals(word)) {
                q1.pollFirst();
            } else if (!q2.isEmpty() && q2.peekFirst().equals(word)) {
                q2.pollFirst();
            } else {
                return "No";
            }
        }
        
        return "Yes";
    }
}