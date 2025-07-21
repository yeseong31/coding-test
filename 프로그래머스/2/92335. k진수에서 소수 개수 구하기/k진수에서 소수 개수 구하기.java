import java.util.Arrays;

class Solution {
    
    private static boolean isPrimeNumber(long n) {
        if (n <= 1) {
            return false;
        }
        
        for (int i = 2; i <= Math.sqrt(n); i++) {
            if (n % i == 0) {
                return false;
            }
        }
        
        return true;
    }
    
    public int solution(int n, int k) {
        int answer = -1;
        
        String converted = Long.toString(n, k);
        String[] numbers = converted.split("0");
        
        return (int) Arrays.stream(numbers)
                .filter(s -> !s.isEmpty())
                .mapToLong(Long::parseLong)
                .filter(v -> isPrimeNumber(v))
                .count();
    }
}