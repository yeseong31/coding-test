import java.util.*;

class Solution {
    
    public int solution(int[] citations) {
        Integer[] arr = Arrays.stream(citations).boxed().toArray(Integer[]::new);
        Arrays.sort(arr, Collections.reverseOrder());
        
        int count = 0;
        
        for (int i = 0; i < arr.length; i++) {
            if (i < arr[i]) {
                count++;
            }
        }
        
        return count;
    }
}