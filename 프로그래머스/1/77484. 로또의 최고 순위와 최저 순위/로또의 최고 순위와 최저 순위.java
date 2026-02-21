import java.util.*;

class Solution {
    
    public int[] solution(int[] lottos, int[] win_nums) {
        int correct = 0;
        int cnt0 = 0;
        
        Set<Integer> winSet = new HashSet<>();
        for (int num : win_nums) {
            winSet.add(num);
        }
        
        for (int lotto : lottos) {
            if (lotto == 0) {
                cnt0++;
            } else if (winSet.contains(lotto)) {
                correct++;
            }
        }
        
        int[] rank = {6, 6, 5, 4, 3, 2, 1};
        
        return new int[] {rank[correct + cnt0], rank[correct]};
    }
}