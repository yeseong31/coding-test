import java.util.ArrayDeque;
import java.util.Deque;
import java.util.HashMap;
import java.util.Map;
import java.util.Stack;

class Solution {
    private final Map<Character, Character> pairs = new HashMap<>() {{
        put(')', '(');
        put(']', '[');
        put('}', '{');
    }};
    
    private boolean isValid(Deque<Character> q) {
        Stack<Character> stack = new Stack<>();
        
        for (char c : q) {
            if (!pairs.containsKey(c)) {
                stack.push(c);
            } else if (!stack.isEmpty() && stack.peek() == pairs.get(c)) {
                stack.pop();
            } else {
                return false;
            }
        }
        
        return stack.isEmpty();
    }
    
    public int solution(String s) {
        int answer = 0;
        Deque<Character> q = new ArrayDeque<>();
        
        for (char c : s.toCharArray()) {
            q.offerLast(c);
        }
        
        for (int i = 0; i < s.length(); i++) {
            if (isValid(q)) {
                answer++;
            }
            q.offerFirst(q.pollLast());
        }
        
        return answer;
    }
}