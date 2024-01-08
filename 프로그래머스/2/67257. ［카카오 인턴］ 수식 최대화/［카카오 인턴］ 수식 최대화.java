import java.util.ArrayList;
import java.util.List;
import java.util.Stack;
import java.util.StringTokenizer;

class Solution {
    
    private static final String[][] PRIORITY_OPERATORS = {
        "+-*".split(""), "+*-".split(""), "-+*".split(""),
        "-*+".split(""), "*+-".split(""), "*-+".split(""),
    };
    
    public long solution(String expression) {
        long answer = 0;
        List<String> tokens = split(expression);
        
        for (String[] operators : PRIORITY_OPERATORS) {
            long result = calculate(expression, operators, tokens);
            answer = Math.max(answer, result);
        }
        
        return answer;
    }
    
    private long calculate(String expression, String[] operators, List<String> tokens) {
        Stack<String> stack = new Stack<>();
        
        for (String operator : operators) {
            for (String token : tokens) {
                if (!stack.empty() && stack.peek().equals(operator)) {
                    String targetOperator = stack.pop();
                    long leftNumber = Long.parseLong(stack.pop());
                    long rightNumber = Long.parseLong(token);

                    long result = calculate(leftNumber, rightNumber, targetOperator);
                    stack.push(String.valueOf(result));
                    continue;
                }
                
                stack.push(token);
            }
            
            tokens = new ArrayList<>(stack);
        }
        
        long result = Long.parseLong(stack.pop());
        return Math.abs(result);
    }
    
    private long calculate(long leftNumber, long rightNumber, String targetOperator) {
        if (targetOperator.equals("+")) {
            return leftNumber + rightNumber;
        }
        if (targetOperator.equals("-")) {
            return leftNumber - rightNumber;
        }
        return leftNumber * rightNumber;
    }
    
    private List<String> split(final String expression) {
        StringTokenizer tokenizer = new StringTokenizer(expression, "+-*", true);
        List<String> tokens = new ArrayList<>();
        
        while (tokenizer.hasMoreTokens()) {
            tokens.add(tokenizer.nextToken());
        }
        
        return tokens;
    }
}