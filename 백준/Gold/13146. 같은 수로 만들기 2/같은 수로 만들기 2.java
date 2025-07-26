import java.io.*;
import java.util.StringTokenizer;

public class Main {

    public static void main(String[] args) throws Exception {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringBuilder sb = new StringBuilder();

        int n = Integer.parseInt(br.readLine());

        long answer = 0;
        int maxNumber = Integer.MIN_VALUE;
        int prevGroupValue = -1;

        for (int i = 0; i < n; i++) {
            int x = Integer.parseInt(br.readLine());
            maxNumber = Math.max(maxNumber, x);

            if (i == 0) {
                prevGroupValue = x;
                continue;
            }

            if (x == prevGroupValue) continue;
            if (prevGroupValue < x) {
                answer += x - prevGroupValue;
            }

            prevGroupValue = x;
        }

        answer += maxNumber - prevGroupValue;

        sb.append(answer);
        bw.write(sb.toString());
        bw.flush();
        bw.close();
    }
}