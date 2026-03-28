import java.util.*;

class Solution {
    
    public int solution(String[] want, int[] number, String[] discount) {
        int answer = 0;

        Map<String, Integer> target = new HashMap<>();
        for (int i = 0; i < want.length; i++) {
            target.put(want[i], number[i]);
        }

        for (int i = 0; i <= discount.length - 10; i++) {
            Map<String, Integer> current = new HashMap<>();
            
            for (int j = i; j < i + 10; j++) {
                current.put(discount[j], current.getOrDefault(discount[j], 0) + 1);
            }

            if (current.equals(target)) {
                answer++;
            }
        }

        return answer;
    }
}