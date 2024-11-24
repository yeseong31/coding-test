import java.util.Stack;

class Solution {

    public int solution(String s) {
        Stack<Character> stack = new Stack<>();
        
        for (char c : s.toCharArray()) {
            if (!stack.isEmpty() && stack.peek() == c) {
                stack.pop();
                continue;
            }
            
            stack.add(c);
        }

        if (stack.isEmpty()) {
            return 1;
        } else {
            return 0;
        }
    }
}