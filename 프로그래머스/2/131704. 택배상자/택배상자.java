import java.util.*;

class Solution {
    
    public int solution(int[] order) {
        List<Integer> answer = new ArrayList<>();
        Stack<Integer> stack = new Stack<>();
        
        int i = 1;
        int j = 0;
        
        while (i <= order.length) {
            while (!stack.isEmpty() && stack.peek() == order[j]) {
                answer.add(stack.pop());
                j++;
            }
            
            if (i != order[j]) {
                stack.push(i);
            } else {
                answer.add(i);
                j++;
            }
            
            i++;
        }
        
        while (!stack.isEmpty() && stack.peek() == order[j]) {
            answer.add(stack.pop());
            j++;
        }
        
        return answer.size();
    }
}