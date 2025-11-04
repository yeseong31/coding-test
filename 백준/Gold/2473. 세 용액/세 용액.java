import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringBuilder sb = new StringBuilder();

        int n = Integer.parseInt(br.readLine());

        StringTokenizer st = new StringTokenizer(br.readLine());
        long[] numbers = new long[n];

        for (int i = 0; i < n; i++) {
            numbers[i] = Integer.parseInt(st.nextToken());
        }

        long[] answer = solution(n, numbers);
        sb.append(answer[0]).append(" ").append(answer[1]).append(" ").append(answer[2]);

        bw.write(sb.toString());
        bw.flush();
        bw.close();
    }

    private static long[] solution(int n, long[] numbers) {
        long[] answer = new long[3];
        long minDiff = Long.MAX_VALUE;

        Arrays.sort(numbers);

        for (int i = 0; i < n; i++) {
            long target = numbers[i];
            int left = 0;
            int right = n - 1;

            while (left < right) {
                long sum = numbers[left] + numbers[right] + target;
                long diff = Math.abs(sum);

                if (diff < minDiff && left != i && right != i) {
                    minDiff = diff;
                    answer[0] = numbers[left];
                    answer[1] = numbers[right];
                    answer[2] = target;
                } else if (sum > 0) {
                    right--;
                } else {
                    left++;
                }
            }
        }

        Arrays.sort(answer);
        return answer;
    }
}