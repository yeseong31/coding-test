import java.util.Stack;
import java.util.stream.Collectors;

class Solution {
    public String solution(String number, int k) {
        Stack<Character> stack = new Stack<>();
        
        for (char n : number.toCharArray()) {
            while (!stack.isEmpty() && stack.peek() < n && k > 0) {
                stack.pop();
                k--;
            }
            stack.add(n);
        }
        
        while (k > 0) {
            stack.pop();
            k--;
        }
        
        return stack.stream()
                .map(String::valueOf)
                .collect(Collectors.joining(""));
    }
}