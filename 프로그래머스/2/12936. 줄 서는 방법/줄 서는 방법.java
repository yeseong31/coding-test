import java.util.*;

class Solution {
    public int[] solution(int n, long k) {
        int[] answer = new int[n];
        List<Integer> nums = new ArrayList<>();
        
        for (int i = 1; i <= n; i++) {
            nums.add(i);
        }
        
        k--;
        
        for (int i = 0; i < n; i++) {
            long fact = factorial(n - 1 - i);
            int index = (int)(k / fact);
            k %= fact;
            answer[i] = nums.remove(index);
        }
        
        return answer;
    }

    private long factorial(int num) {
        long result = 1;
        for (int i = 2; i <= num; i++) {
            result *= i;
        }
        return result;
    }
}