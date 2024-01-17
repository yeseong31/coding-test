import java.util.Stack;

class Solution {
    public int[] solution(int[] prices) {
        int[] answer = new int[prices.length];
        Stack<Integer> stack = new Stack<>();
        
        for (int index = 0; index < prices.length; index++) {
            while (!stack.isEmpty() && prices[stack.peek()] > prices[index]) {
                int target = stack.pop();
                answer[target] = index - target;
            }
            
            stack.add(index);
        }
        
        for (int n : stack) {
            answer[n] = (prices.length - 1) - n;
        }
        
        return answer;
    }
}