import java.io.*;
import java.util.StringTokenizer;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int k = Integer.parseInt(st.nextToken());

        int a = getMinimumACount(n, k);
        int b = n - a;
        
        if (a == -1) {
            System.out.println(-1);
            return;
        }

        for (int i = 0; i < n; i++) {
            if (a == 0 || k < b) {
                sb.append('B');
                b--;
            } else {
                sb.append('A');
                k -= b;
                a--;
            } 
        }

        System.out.println(sb);
    }

    private static int getMinimumACount(int n, int k) {
        int a = 1;
        int b = n - 1;

        while (a * b < k) {
            if (b < 0) return -1;
            a++;
            b--;
        }

        return a;
    }
}