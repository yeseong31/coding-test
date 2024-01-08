import java.util.ArrayList;
import java.util.HashSet;
import java.util.List;
import java.util.Set;
import java.util.stream.Collectors;

class Solution {
    public int solution(String numbers) {
        List<Integer> remainNumbers = numbers.chars()
                .map(c -> c - '0')
                .boxed()
                .collect(Collectors.toList());
        
        Set<Integer> combinations = new HashSet<>();
        makeCombinations(0, remainNumbers, new boolean[numbers.length()], combinations);
        
        return countPrimeNumbers(combinations);
    }
    
    private int countPrimeNumbers(Set<Integer> combinations) {
        long result = combinations.stream()
            .filter(n -> isPrimeNumber(n))
            .count();
        
        return Long.valueOf(result).intValue();
    }
    
    private boolean isPrimeNumber(Integer number) {
        if (number < 2) {
            return false;
        }
        
        for (int x = 2; x <= (int) Math.sqrt(number); x++) {
            if (number % x == 0) {
                return false;
            }
        }
        
        return true;
    }
    
    private void makeCombinations(int target, List<Integer> remainNumbers, boolean[] used, Set<Integer> combinations) {
        if (isPrimeNumber(target)) {
            combinations.add(target);
        }
        
        for (int index = 0; index < remainNumbers.size(); index++) {
            if (used[index]) {
                continue;
            }
            
            int nextTarget = target * 10 + remainNumbers.get(index);
            
            used[index] = true;
            makeCombinations(nextTarget, remainNumbers, used, combinations);
            used[index] = false;
        }
    }
}
