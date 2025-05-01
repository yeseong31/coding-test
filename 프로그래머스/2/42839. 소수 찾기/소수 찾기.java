import java.util.HashSet;
import java.util.Set;


class Solution {
    private boolean isPrimeNumber(int x) {
        if (x <= 1) {
            return false;
        }
        
        for (int i = 2; i <= Math.sqrt(x); i++) {
            if (x % i == 0) {
                return false;
            }
        }
        
        return true;
    }
    
    private void getPrimeNums(int acc, int[] nums, boolean[] isUsed, Set<Integer> result) {
        if (isPrimeNumber(acc)) {
            result.add(acc);
        }
        
        for (int i = 0; i < nums.length; i++) {
            if (isUsed[i]) {
                continue;
            }
            
            int newAcc = acc * 10 + nums[i];
            
            isUsed[i] = true;
            getPrimeNums(newAcc, nums, isUsed, result);
            isUsed[i] = false;
        }
    }
    
    public int solution(String numbers) {
        Set<Integer> result = new HashSet<>();
        
        int[] nums = numbers.chars()
                .map(c -> Character.getNumericValue(c))
                .toArray();
        
        getPrimeNums(0, nums, new boolean[nums.length], result);
        return result.size();
    }
}