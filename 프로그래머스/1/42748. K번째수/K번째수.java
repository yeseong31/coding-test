import java.util.Arrays;
import java.util.ArrayList;
import java.util.List;


class Solution {
    public int[] solution(int[] array, int[][] commands) {
        List<Integer> answer = new ArrayList<>();
        
        for (int[] command : commands) {
            int startIndex = command[0] - 1;
            int endIndex = command[1];
            int targetIndex = command[2] - 1;
            
            int[] subArray = Arrays.copyOfRange(array, startIndex, endIndex);
            Arrays.sort(subArray);
            answer.add(subArray[targetIndex]);
        }
        
        return answer.stream()
                .mapToInt(Integer::intValue)
                .toArray();
    }
}