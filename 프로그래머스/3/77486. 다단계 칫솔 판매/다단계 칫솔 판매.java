import java.util.*;

class Solution {
    
    public int[] solution(String[] enroll, String[] referral, String[] seller, int[] amount) {
        Map<String, String> parentMap = new HashMap<>();
        Map<String, Integer> totalProfit = new HashMap<>();

        for (int i = 0; i < enroll.length; i++) {
            parentMap.put(enroll[i], referral[i]);
        }

        for (int i = 0; i < seller.length; i++) {
            String current = seller[i];
            int money = amount[i] * 100;

            while (!current.equals("-") && money > 0) {
                int tax = money / 10;
                int mine = money - tax;

                totalProfit.put(current, totalProfit.getOrDefault(current, 0) + mine);

                current = parentMap.get(current);
                money = tax;
            }
        }

        int[] answer = new int[enroll.length];
        for (int i = 0; i < enroll.length; i++) {
            answer[i] = totalProfit.getOrDefault(enroll[i], 0);
        }

        return answer;
    }
}