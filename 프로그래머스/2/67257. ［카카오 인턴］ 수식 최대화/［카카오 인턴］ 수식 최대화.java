import java.util.ArrayList;
import java.util.ArrayDeque;
import java.util.Deque;
import java.util.List;
import java.util.StringTokenizer;


class Solution {
    private static final String[][] priorityOps = {
        "+-*".split(""),
        "+*-".split(""),
        "-+*".split(""),
        "-*+".split(""),
        "*+-".split(""),
        "*-+".split(""),
    };
    
    private long calculate(long n1, long n2, String op) {
        return switch (op) {
                case "+" -> n1 + n2;
                case "-" -> n1 - n2;
                case "*" -> n1 * n2;
                default -> 0;
        };
    }
    
    private long calculate(Deque<String> tokens, String[] ops) {
        Deque<String> queue = new ArrayDeque<>(tokens);
        
        for (String op : ops) {
            Deque<String> tmpQueue = new ArrayDeque<>();
            
            while (!queue.isEmpty()) {
                String token = queue.pollFirst();
                
                if (token.equals(op)) {
                    long n1 = Long.parseLong(tmpQueue.pollLast());
                    long n2 = Long.parseLong(queue.pollFirst());
                    long result = calculate(n1, n2, op);
                    tmpQueue.add(Long.toString(result));
                } else {
                    tmpQueue.add(token);
                }
            }
            
            queue = new ArrayDeque<>(tmpQueue);
        }
        
        return Long.parseLong(queue.pollFirst());
    }
    
    public long solution(String expression) {
        long answer = Long.MIN_VALUE;
        
        StringTokenizer tokenizer = new StringTokenizer(expression, "+-*", true);
        Deque<String> tokens = new ArrayDeque<>();
        
        while (tokenizer.hasMoreTokens()) {
            tokens.add(tokenizer.nextToken());
        }
        
        for (String[] ops : priorityOps) {
            long absValue = Math.abs(calculate(tokens, ops));
            answer = Math.max(answer, absValue);
        }
        
        return answer;
    }
}