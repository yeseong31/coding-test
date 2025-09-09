import java.io.*;
import java.util.StringTokenizer;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringBuilder sb = new StringBuilder();

        int n = Integer.parseInt(br.readLine());

        StringTokenizer st = new StringTokenizer(br.readLine());
        int[] A = new int[n];

        for (int i = 0; i < n; i++) {
            A[i] = Integer.parseInt(st.nextToken());
        }

        int answer = solution(n, A);
        sb.append(answer);

        bw.write(sb.toString());
        bw.flush();
        bw.close();
    }

    private static int solution(int n, int[] A) {
        int[] incDp = new int[n];
        int[] decDp = new int[n];

        for (int i = 0; i < n; i++) {
            incDp[i] = 1;
            for (int j = 0; j < i; j++) {
                if (A[j] < A[i]) {
                    incDp[i] = Math.max(incDp[i], incDp[j] + 1);
                }
            }
        }

        for (int i = n - 1; i >= 0; i--) {
            decDp[i] = 1;
            for (int j = n - 1; j > i; j--) {
                if (A[j] < A[i]) {
                    decDp[i] = Math.max(decDp[i], decDp[j] + 1);
                }
            }
        }

        int answer = 0;
        for (int i = 0; i < n; i++) {
            answer = Math.max(answer, incDp[i] + decDp[i] - 1);
        }
        return answer;
    }
}