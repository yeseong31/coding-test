import java.io.*;
import java.util.StringTokenizer;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringBuilder sb = new StringBuilder();

        int n = Integer.parseInt(br.readLine());
        int[][] colors = new int[n][3];

        for (int i = 0; i < n; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            colors[i][0] = Integer.parseInt(st.nextToken());
            colors[i][1] = Integer.parseInt(st.nextToken());
            colors[i][2] = Integer.parseInt(st.nextToken());
        }

        for (int i = 1; i < n; i++) {
            colors[i][0] += Math.min(colors[i - 1][1], colors[i - 1][2]);
            colors[i][1] += Math.min(colors[i - 1][2], colors[i - 1][0]);
            colors[i][2] += Math.min(colors[i - 1][0], colors[i - 1][1]);
        }

        int answer = Math.min(Math.min(colors[n - 1][0], colors[n - 1][1]), colors[n - 1][2]);
        sb.append(answer);

        bw.write(sb.toString());
        bw.flush();
        bw.close();
    }
}