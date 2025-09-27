import java.io.*;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Solution {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringBuilder sb = new StringBuilder();

        int T = Integer.parseInt(br.readLine());

        for (int testCase = 1; testCase <= T; testCase++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int n = Integer.parseInt(st.nextToken());
            long m = Long.parseLong(st.nextToken());

            st = new StringTokenizer(br.readLine());
            long[] candies = new long[n];
            long sum = 0;
            for (int i = 0; i < n; i++) {
                candies[i] = Long.parseLong(st.nextToken());
                sum += candies[i];
            }

            long answer = 0;
            long left = 1;
            long right = Arrays.stream(candies).max().orElse(0);

            while (left <= right) {
                long mid = left + (right - left) / 2;
                if (isPossible(candies, mid, m)) {
                    answer = mid;
                    left = mid + 1;
                } else {
                    right = mid - 1;
                }
            }

            sb.append('#').append(testCase).append(' ').append(answer).append('\n');
        }

        bw.write(sb.toString());
        bw.flush();
        bw.close();
    }

    private static boolean isPossible(long[] candies, long k, long m) {
        if (k == 0) return false;

        long total = 0;
        for (long c : candies) {
            total += c / k;
            if (total >= m) return true;
        }
        return total >= m;
    }
}