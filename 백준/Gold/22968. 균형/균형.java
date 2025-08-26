import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;

public class Main {

    private static final int MAX_HEIGHT = 50;

    private static long solution(long n) {
        int answer = 0;

        long[] dp = new long[MAX_HEIGHT + 1];
        dp[1] = 1;
        dp[2] = 2;

        // 
        for (int h = 2; h <= MAX_HEIGHT; h++) {
            dp[h] = dp[h - 1] + dp[h - 2] + 1;
        }

        for (int h = 0; h <= MAX_HEIGHT; h++) {
            if (dp[h] <= n) {
                answer = h;
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
            sb.append(solution(n)).append("\n");
        }

        bw.write(sb.toString());
        bw.flush();
        bw.close();
    }
}