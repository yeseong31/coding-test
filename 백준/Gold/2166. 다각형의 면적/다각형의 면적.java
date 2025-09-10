import java.io.*;
import java.util.StringTokenizer;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringBuilder sb = new StringBuilder();

        int n = Integer.parseInt(br.readLine());
        int[] x = new int[n];
        int[] y = new int[n];

        for (int i = 0; i < n; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            x[i] = Integer.parseInt(st.nextToken());
            y[i] = Integer.parseInt(st.nextToken());
        }

        double answer = 0;

        for (int i = 1; i < n; i++) {
            answer += calculateCCW(x[0], x[i - 1], x[i], y[0], y[i - 1], y[i]);
        }

        String message = String.format("%.1f", Math.abs(answer));

        sb.append(message);
        bw.write(sb.toString());
        bw.flush();
        bw.close();
    }

    private static double calculateCCW(double x1, double x2, double x3, double y1, double y2, double y3) {
        double answer = (x1 * y2 + x2 * y3 + x3 * y1) - (x2 * y1 + x3 * y2 + x1 * y3);
        return answer * 0.5;
    }
}