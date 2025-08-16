import java.io.*;

public class Solution {

    private static int solution(int n) {
        int count = 1;
        int total = (1 << 10) - 1;  // '1111111111'
        int mask = 0;

        while (mask != total) {
            for (char c : String.valueOf(n * count++).toCharArray()) {
                mask |= (1 << (c - '0'));
            }
        }
        return n * (count - 1);
    }

    public static void main(String[] args) throws Exception {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringBuilder sb = new StringBuilder();

        int T = Integer.parseInt(br.readLine());
        for (int testCase = 1; testCase <= T; testCase++) {
            int n = Integer.parseInt(br.readLine());

            String message = String.format("#%d %d%n", testCase, solution(n));
            sb.append(message);
        }

        bw.write(sb.toString());
        bw.flush();
        bw.close();
    }
}