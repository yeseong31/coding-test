import java.util.ArrayList;
import java.util.List;


class Solution {
    private static final int[][] persons = new int[][] {
        {1, 2, 3, 4, 5},
        {2, 1, 2, 3, 2, 4, 2, 5},
        {3, 3, 1, 1, 2, 2, 4, 4, 5, 5},
    };
    
    public int[] solution(int[] answers) {
        int[] count = new int[] {0, 0, 0};
        
        for (int i = 0; i < 3; i++) {
            for (int j = 0; j < answers.length; j++) {
                if (persons[i][j % persons[i].length] == answers[j]) {
                    count[i]++;
                }
            }
        }
        
        int maxCount = -1;
        for (int i = 0; i < count.length; i++) {
            if (maxCount < count[i]) {
                maxCount = count[i];
            }
        }
        
        List<Integer> result = new ArrayList<>();
        for (int i = 0; i < count.length; i++) {
            if (count[i] == maxCount) {
                result.add(i + 1);
            }
        }
        
        return result.stream()
            .mapToInt(i -> i)
            .toArray();
    }
}