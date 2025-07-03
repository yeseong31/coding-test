import java.util.HashSet;
import java.util.Set;

class Solution {
    private final Set<Integer> primeSet = new HashSet<>();
    
    private void generatePermutations(String current, String numbers, boolean[] visited) {
        if (!current.isEmpty()) {
            int num = Integer.parseInt(current);
            if (isPrime(num)) {
                primeSet.add(num);
            }
        }

        for (int i = 0; i < numbers.length(); i++) {
            if (!visited[i]) {
                visited[i] = true;
                generatePermutations(current + numbers.charAt(i), numbers, visited);
                visited[i] = false;
            }
        }
    }

    private boolean isPrime(int number) {
        if (number < 2) return false;
        if (number == 2) return true;
        if (number % 2 == 0) return false;

        for (int i = 3; i <= Math.sqrt(number); i += 2) {
            if (number % i == 0) return false;
        }

        return true;
    }
    
    public int solution(String numbers) {
        boolean[] visited = new boolean[numbers.length()];
        generatePermutations("", numbers, visited);
        return primeSet.size();
    }
}