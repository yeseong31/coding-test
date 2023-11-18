import java.util.Arrays;
import java.util.Collections;


class Solution {
    public int solution(int[] citations) {
        Integer[] numbers = Arrays.stream(citations)
                .boxed()
                .toArray(Integer[]::new);
        
        Arrays.sort(numbers, Collections.reverseOrder());
        
        for (int i = 0; i < numbers.length; i++) {
            if (i >= numbers[i]) {
                return i;
            }
        }
        
        return numbers.length;
    }
}