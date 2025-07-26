import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.Stack;
import java.util.StringTokenizer;

public class Main {

    private static int solution(int[] points) {
        int answer = 0;
        Stack<Integer> stack = new Stack<>();

        for (int point : points) {
            int height = point;

            while (!stack.isEmpty() && stack.peek() > point) {
                if (stack.peek() != height) {
                    answer++;
                    height = stack.peek();
                }
                stack.pop();
            }

            stack.add(point);
        }

        return answer;
    }

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringBuilder sb = new StringBuilder();

        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());

        int[] points = new int[n + 1];
        int tmp;

        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            tmp = Integer.parseInt(st.nextToken());
            points[i] = Integer.parseInt(st.nextToken());
        }
        points[n] = 0;

        int answer = solution(points);
        sb.append(answer);

        bw.write(sb.toString());
        bw.flush();
        bw.close();
    }
}