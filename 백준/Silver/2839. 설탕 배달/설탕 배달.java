import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());
        int[] d = new int[n + 1];
        Arrays.fill(d, 5001);
        d[0] = 0;

        for (int i : new int[]{3, 5}) {
            for (int j = i; j <= n; j++) {
                d[j] = Math.min(d[j], d[j - i] + 1);
            }
        }

        System.out.println(d[n] != 5001 ? d[n] : -1);
    }
}