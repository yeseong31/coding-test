import java.lang.StringBuilder;
import java.util.Arrays;

class Solution {
    
    public int solution(int n, int k) {
        String[] target = convertToK(n, k).split("0");
        return countPrimeNumber(target);
    }
    
    private int countPrimeNumber(String[] target) {
        return (int) Arrays.stream(target)
                .filter(s -> !s.isEmpty())
                .mapToLong(Long::parseLong)
                .filter(this::isPrimeNumber)
                .count();
    }
    
    private boolean isPrimeNumber(long number) {
        for (int index = 2; index <= Math.sqrt(number); index++) {
            if (number % index == 0) {
                return false;
            }
        }
        
        return number > 1;
    }
    
    private String convertToK(int n, int k) {
        StringBuilder sb = new StringBuilder();
        
        while (n != 0) {
            sb.append(n % k);
            n /= k;
        }    
        
        return sb.reverse().toString();
    }
}