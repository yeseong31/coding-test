import java.io.*;
import java.util.Stack;
import java.util.StringTokenizer;

public class Main {

    public static void main(String[] args) throws Exception {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringBuilder sb = new StringBuilder();

        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());

        long answer = 0;
        int maxNumber = Integer.MIN_VALUE;
        int x;

        Stack<Integer> stack = new Stack<>();

        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            x = Integer.parseInt(st.nextToken());

            maxNumber = Math.max(maxNumber, x);

            if (stack.isEmpty()) {
                stack.add(x);
                continue;
            }

            if (stack.peek() == x) continue;
            if (stack.peek() < x) {
                answer += x - stack.pop();
            }

            stack.add(x);
        }

        if (!stack.isEmpty()) {
            answer += maxNumber - stack.peek();
        }

        sb.append(answer);

        bw.write(sb.toString());
        bw.flush();
        bw.close();
    }
}