import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Stack;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String exp = br.readLine();

        StringBuilder sb = new StringBuilder();
        Stack<Character> ops = new Stack<>();

        for (int i = 0; i < exp.length(); i++) {
            char c = exp.charAt(i);

            if (Character.isAlphabetic(c)) {
                sb.append(c);
                continue;
            }

            if (c == '(') {
                ops.push(c);
                continue;
            }

            if (c == ')') {
                while (!ops.isEmpty() && ops.peek() != '(') {
                    sb.append(ops.pop());
                }
                if (!ops.isEmpty()) {
                    ops.pop();
                }
                continue;
            }

            if (isOperator(c)) {
                while (!ops.isEmpty() && ops.peek() != '(' && getPrecedence(ops.peek()) >= getPrecedence(c)) {
                    sb.append(ops.pop());
                }
                ops.push(c);
            }
        }

        while (!ops.isEmpty()) {
            sb.append(ops.pop());
        }

        System.out.println(sb);
    }

    private static boolean isOperator(char c) {
        return c == '+' || c == '-' || c == '*' || c == '/';
    }

    private static int getPrecedence(char op) {
        switch (op) {
            case '+':
            case '-':
                return 1;
            case '*':
            case '/':
                return 2;
            default:
                return 0;
        }
    }
}