import java.util.ArrayList;
import java.util.HashSet;
import java.util.List;
import java.util.Set;
import java.util.stream.Collectors;


class Solution {
    public int solution(String numbers) {
        Set<Integer> primes = new HashSet<>();
        int[] remainNumbers = numbers.chars()
            .map(n -> Character.getNumericValue(n))
            .toArray();
        
        dfs(0, remainNumbers, new boolean[numbers.length()], primes);
        return primes.size();
    }
    
    private void dfs(int number, int[] remainNumbers, boolean[] visited, Set<Integer> primes) {
        if (isPrime(number)) {
            primes.add(number);
        }
        
        for (int i = 0; i < remainNumbers.length; i++) {
            if (visited[i]) {
                continue;
            }
            int nextNumber = number * 10 + remainNumbers[i];
            visited[i] = true;
            dfs(nextNumber, remainNumbers, visited, primes);
            visited[i] = false;
        }
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