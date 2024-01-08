import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

class Solution {
    public int[] solution(int[] array, int[][] commands) {
        List<Integer> answer = new ArrayList<>();
        
        for (int[] command : commands) {
            int i = command[0];
            int j = command[1];
            int k = command[2];
            
            int[] copiedArray = Arrays.copyOfRange(array, i - 1, j);
            Arrays.sort(copiedArray);
            
            answer.add(copiedArray[k - 1]);
        }
        
        return answer.stream()
                .mapToInt(n -> n)
                .toArray();
    }
}