import java.util.ArrayList;
import java.util.HashSet;
import java.util.List;
import java.util.Set;
import java.util.stream.Collectors;


class Solution {
    public int solution(String numbers) {
        List<Integer> remainNumbers = numbers.chars()
            .map(n -> Character.getNumericValue(n))
            .boxed()
            .collect(Collectors.toList());
        
        return dfs(0, remainNumbers).size();
    }
    
    private Set<Integer> dfs(int number, List<Integer> remainNumbers) {
        Set<Integer> result = new HashSet<>();
        
        if (isPrime(number)) {
            result.add(number);
        }
        
        for (int i = 0; i < remainNumbers.size(); i++) {
            int nextNumber = number * 10 + remainNumbers.get(i);
            List<Integer> nextRemainNumbers = new ArrayList<>(remainNumbers);
            nextRemainNumbers.remove(i);
            result.addAll(dfs(nextNumber, nextRemainNumbers));
        }
        
        return result;
    }
    
    private boolean isPrime(int number) {
        if (number <= 1) {
            return false;
        }
        for (int i = 2; i <= Math.sqrt(number); i++) {
            if (number % i == 0) {
                return false;
            }
        }
        return true;
    }
}