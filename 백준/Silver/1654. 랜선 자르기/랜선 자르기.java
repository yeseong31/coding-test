import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.*;

public class Main {

    private static long solution(int n, int k, int[] lines) {
        long answer = 0;
        long left = 1;
        long right = Arrays.stream(lines).max().getAsInt();

        while (left <= right) {
            long mid = left + (right - left) / 2;
            long count = 0;

            for (int line : lines) {
                count += line / mid;
                if (count >= k) {
                    break;
                }
            }

            if (count >= k) {
                answer = mid;
                left = mid + 1;
            } else {
                right = mid - 1;
            }
        }

        return answer;
    }

    public static void main(String[] args) throws Exception {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringBuilder sb = new StringBuilder();

        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int k = Integer.parseInt(st.nextToken());

        int[] lines = new int[n];
        for (int i = 0; i < n; i++) {
            lines[i] = Integer.parseInt(br.readLine());
        }

        long answer = solution(n, k, lines);
        sb.append(answer);

        bw.write(sb.toString());
        bw.flush();
        bw.close();
    }
}