import java.util.Stack;

class Solution {
    boolean solution(String s) {
        Stack<Character> stack = new Stack<>();
        
        for (char c : s.toCharArray()) {
            if (stack.isEmpty() || c == '(') {
                stack.add(c);
                continue;
            }
            if (stack.peek() == '(') {
                stack.pop();
            }
        }

        return stack.isEmpty();
    }
}