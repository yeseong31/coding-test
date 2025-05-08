import java.util.ArrayList;
import java.util.Collections;
import java.util.HashSet;
import java.util.List;
import java.util.Set;

class Solution {
    public int[] solution(int[] numbers) {
        Set<Integer> cases = new HashSet<>();
        
        for (int i = 0; i < numbers.length - 1; i++) {
            for (int j = i + 1; j < numbers.length; j++) {
                cases.add(numbers[i] + numbers[j]);
            }
        }
        
        List<Integer> answer = new ArrayList<>(List.copyOf(cases));
        return answer.stream()
                .sorted()
                .mapToInt(Integer::intValue)
                .toArray();
    }
}