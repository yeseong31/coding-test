import java.util.*;

class Solution {
    
    public int[] solution(String msg) {
        List<Integer> answer = new ArrayList<>();
        Map<String, Integer> dic = new HashMap<>();
        
        int n = 1;
        for (char ch = 'A'; ch <= 'Z'; ch++) {
            dic.put(String.valueOf(ch), n++);
        }
        
        int p = 0;
        int c = 0;
        
        while (true) {
            c++;
            
            if (c == msg.length()) {
                answer.add(dic.get(msg.substring(p)));
                break;
            }
            
            String next = msg.substring(p, c + 1);
            
            if (!dic.containsKey(next)) {
                dic.put(next, n++);
                answer.add(dic.get(msg.substring(p, c)));
                p = c;
            }
        }
        
        int[] result = new int[answer.size()];
        for (int i = 0; i < answer.size(); i++) {
            result[i] = answer.get(i);
        }
        
        return result;
    }
}