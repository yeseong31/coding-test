import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;

public class Solution {

    private static long solution(long n) {
        long answer = 0;

        while (n != 2) {
            long k = (long) Math.sqrt(n);
            answer++;

            if (k * k == n) {
                n = k;
            } else {
                answer += (k + 1) * (k + 1) - n;
                n = k + 1;
            }
        }

        return answer;
    }

    public static void main(String[] args) throws Exception {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringBuilder sb = new StringBuilder();

        int T = Integer.parseInt(br.readLine());

        for (int testCase = 1; testCase <= T; testCase++) {
            long n = Long.parseLong(br.readLine());
            String message = String.format("#%d %d%n", testCase, solution(n));
            sb.append(message);
        }

        bw.write(sb.toString());
        bw.flush();
        bw.close();
    }
}