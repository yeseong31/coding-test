import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.Arrays;
import java.util.Stack;
import java.util.StringTokenizer;

public class Main {

    private static final int INF = 100_001;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringBuilder sb = new StringBuilder();

        int n = Integer.parseInt(br.readLine());
        int[] heights = new int[n];

        StringTokenizer st = new StringTokenizer(br.readLine());
        for (int i = 0; i < n; i++) {
            heights[i] = Integer.parseInt(st.nextToken());
        }

        int[][] answer = solution(n, heights);
        for (int i = 0; i < n; i++) {
            sb.append(answer[i][0]);
            if (answer[i][0] != 0) {
                sb.append(" ").append(answer[i][1]);
            }
            sb.append("\n");
        }

        bw.write(sb.toString());
        bw.flush();
        bw.close();
    }

    private static int[][] solution(int n, int[] heights) {
        int[][] answer = new int[n][2];
        int[] counts = new int[n + 1];
        int[] closest = new int[n + 1];

        Arrays.fill(closest, INF);

        Stack<Building> stack = new Stack<>();
        for (int i = 0; i < n; i++) {
            int number = i + 1;
            int height = heights[i];

            Building curr = new Building(number, height);
            while (!stack.isEmpty() && stack.peek().height <= height) {
                stack.pop();
            }

            if (!stack.isEmpty()) {
                counts[number] += stack.size();
                closest[number] = stack.peek().number;
            }

            stack.push(curr);
        }

        stack = new Stack<>();
        for (int i = n - 1; i >= 0; i--) {
            int number = i + 1;
            int height = heights[i];

            Building curr = new Building(number, height);
            while (!stack.isEmpty() && stack.peek().height <= height) {
                stack.pop();
            }

            if (!stack.isEmpty()) {
                counts[number] += stack.size();

                int candidate = stack.peek().number;

                if (closest[number] == INF) {
                    closest[number] = candidate;
                } else {
                    int leftDist = Math.abs(number - closest[number]);
                    int rightDist = Math.abs(candidate - number);

                    if (rightDist < leftDist || (rightDist == leftDist && candidate < closest[number])) {
                        closest[number] = candidate;
                    }
                }
            }

            stack.push(curr);
        }

        for (int i = 1; i <= n; i++) {
            answer[i - 1][0] = counts[i];
            answer[i - 1][1] = (closest[i] == INF) ? 0 : closest[i];
        }

        return answer;
    }

    private static class Building {
        final int number;
        final int height;

        Building(int number, int height) {
            this.number = number;
            this.height = height;
        }
    }
}