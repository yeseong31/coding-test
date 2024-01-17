import java.util.HashMap;
import java.util.LinkedList;
import java.util.Map;
import java.util.Queue;
import java.util.Stack;
import java.util.stream.Collectors;

class Solution {
    
    private final Map<Character, Character> parentheses = new HashMap<>() {{
        put(')', '(');
        put(']', '[');
        put('}', '{');
    }};
    
    public int solution(String s) {
        int answer = 0;
        Queue<Character> queue = new LinkedList<>();
        
        for (char c : s.toCharArray()) {
            queue.offer(c);
        }
        
        for (int x = 0; x < s.length(); x++) {
            String target = convertToString(queue);
            
            if (validate(target)) {
                answer++;
            }
            
            rotate(queue);
        }
        
        return answer;
    }
    
    private void rotate(Queue<Character> queue) {
        queue.offer(queue.poll());
    }
    
    private boolean validate(String target) {
        Stack<Character> stack = new Stack<>();
        
        for (Character c : target.toCharArray()) {
            if (stack.isEmpty() || !parentheses.containsKey(c)) {
                stack.add(c);
                continue;
            }
            if (stack.peek() == parentheses.get(c)) {
                stack.pop();
            }
        }
        
        return stack.isEmpty();
    }
    
    private String convertToString(Queue<Character> queue) {
        return queue.stream()
                .map(String::valueOf)
                .collect(Collectors.joining());
    }
}