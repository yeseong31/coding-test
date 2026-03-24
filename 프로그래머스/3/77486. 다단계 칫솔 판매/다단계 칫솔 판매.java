import java.util.*;

class Solution {
    
    public int[] solution(String[] enroll, String[] referral, String[] seller, int[] amount) {
        Map<String, String> graph = new HashMap<>();
        Map<String, Integer> score = new HashMap<>();
        
        for (int i = 0; i < enroll.length; i++) {
            graph.put(enroll[i], referral[i]);
            score.put(enroll[i], 0);
        }
        
        for (int i = 0; i < seller.length; i++) {
            String s = seller[i];
            int w = amount[i] * 100;
            
            while (w > 0 && !s.equals("-")) {
                int profit = w - w / 10;
                score.put(s, score.get(s) + profit);
                w /= 10;
                s = graph.get(s);
            }
        }
        
        int[] answer = new int[enroll.length];
        for (int i = 0; i < enroll.length; i++) {
            answer[i] = score.get(enroll[i]);
        }
        
        return answer;
    }
}