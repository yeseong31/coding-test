import java.util.ArrayList;
import java.util.List;
import java.util.Stack;
import java.util.StringTokenizer;

class Solution {
    private static final String[][] priorityOperators = {
        "+-*".split(""),
        "+*-".split(""),
        "-+*".split(""),
        "-*+".split(""),
        "*+-".split(""),
        "*-+".split(""),
    };
    
    private static List<String> getTokens(String expression) {
        List<String> result = new ArrayList<>();
        
        StringTokenizer st = new StringTokenizer(expression, "+*-", true);
        while (st.hasMoreTokens()) {
            result.add(st.nextToken());
        }
        
        return result;
    }
    
    private static String calculate(String numStr1, String numStr2, String op) {
        Long number1 = Long.parseLong(numStr1);
        Long number2 = Long.parseLong(numStr2);
        
        switch (op) {
            case "+": return String.valueOf(number1 + number2);
            case "-": return String.valueOf(number1 - number2);
            case "*": return String.valueOf(number1 * number2);
            default: return "0";
        }
    }
    
    private static long calculate(List<String> tokens, String[] ops) {
        List<String> expr = new ArrayList<>(tokens);
    
        for (String op : ops) {
            Stack<String> stack = new Stack<>();
            
            for (int i = 0; i < expr.size(); i++) {
                String token = expr.get(i);
                
                if (token.equals(op)) {
                    String prev = stack.pop();
                    String next = expr.get(++i);
                    stack.add(calculate(prev, next, op));
                } else {
                    stack.add(token);
                }
            }
            
            expr = new ArrayList<>(stack);
        }

        Long result = Long.parseLong(expr.get(0));
        return Math.abs(result);
    }
    
    public long solution(String expression) {
        long answer = 0;
        List<String> tokens = getTokens(expression);
        
        for (String[] ops : priorityOperators) {
            answer = Math.max(answer, calculate(tokens, ops));
        }
        
        return answer;
    }
}