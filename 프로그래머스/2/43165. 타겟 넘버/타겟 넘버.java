import java.util.ArrayList;
import java.util.List;

class Solution {
    private void dfs(int seq, int target, int[] numbers, List<Integer> result) {
        if (seq == numbers.length) {
            result.add(target == 0 ? 1 : 0);
            return;
        }
        
        dfs(seq + 1, target + numbers[seq], numbers, result);
        dfs(seq + 1, target - numbers[seq], numbers, result);
    }
    
    public int solution(int[] numbers, int target) {
        List<Integer> answer = new ArrayList<>();
        dfs(0, target, numbers, answer);
        return (int) answer.stream().filter(x -> x == 1).count();
    }
}