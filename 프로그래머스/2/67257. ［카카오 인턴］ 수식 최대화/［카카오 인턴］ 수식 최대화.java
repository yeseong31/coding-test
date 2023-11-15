import java.util.ArrayList;
import java.util.List;
import java.util.Objects;
import java.util.StringTokenizer;
import java.util.regex.Matcher;
import java.util.regex.Pattern;


class Solution {
    public long solution(String expression) {
        List<String> separateExpression = separateExpression(expression);
        List<String> priorityOps = receivePriorityOps();

        return receiveResult(separateExpression, priorityOps);
    }

    private long receiveResult(List<String> separateExpression, List<String> priorityOps) {
        long result = 0;
        for (String priorityOp : priorityOps) {
            long tmp = calculate(
                    new ArrayList<>(separateExpression), 
                    priorityOp);
            result = Math.max(
                    result, 
                    Math.abs(tmp));
        }
        return result;
    }

    private long calculate(List<String> exp, String priorityOp) {
        for (char op : priorityOp.toCharArray()) {
            for (int index = 0; index < exp.size(); index++) {
                if (!exp.get(index).equals(String.valueOf(op))) {
                    continue;
                }
                long leftNumber = Long.parseLong(exp.get(index - 1));
                long rightNumber = Long.parseLong(exp.get(index + 1));
                long result = compute(leftNumber, rightNumber, op);
                exp.remove(index - 1);
                exp.remove(index - 1);
                exp.remove(index - 1);
                exp.add(index - 1, String.valueOf(result));
                index -= 2;
            }
        }
        return Long.parseLong(exp.get(0));
    }

    private long compute(long num1, long num2, char op) {
        if (op == '+') {
            return num1 + num2;
        }
        if (op == '-') {
            return num1 - num2;
        }
        if (op == '*') {
            return num1 * num2;
        }
        return 0;
    }

    private List<String> separateExpression(String expression) {
        List<String> result = new ArrayList<>();
        Matcher matcher = Pattern.compile("[+\\-*/]").matcher(expression);

        int prevIndex = 0;
        while (matcher.find()) {
            int currentIndex = matcher.start();
            if (currentIndex > 0) {
                result.add(expression.substring(prevIndex, currentIndex).trim());
            }
            result.add(matcher.group().trim());
            prevIndex = matcher.end();
        }

        if (prevIndex < expression.length()) {
            result.add(expression.substring(prevIndex).trim());
        }

        return result;
    }

    private List<String> receivePriorityOps() {
        return List.of("+-*", "+*-", "-+*", "-*+", "*+-", "*-+");
    }
}