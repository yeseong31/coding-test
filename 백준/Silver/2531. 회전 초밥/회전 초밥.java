import java.io.*;
import java.util.StringTokenizer;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int d = Integer.parseInt(st.nextToken());
        int k = Integer.parseInt(st.nextToken());
        int c = Integer.parseInt(st.nextToken());

        int[] sushi = new int[n];
        for (int i = 0; i < n; i++) {
            sushi[i] = Integer.parseInt(br.readLine());
        }

        int[] count = new int[d + 1];
        int unique = 0;

        for (int i = 0; i < k; i++) {
            if (count[sushi[i]] == 0) unique++;
            count[sushi[i]]++;
        }

        int max = unique + (count[c] == 0 ? 1 : 0);

        for (int i = 1; i < n; i++) {
            int remove = sushi[i - 1];
            int add = sushi[(i + k - 1) % n];

            count[remove]--;
            if (count[remove] == 0) unique--;

            if (count[add] == 0) unique++;
            count[add]++;

            int currentMax = unique + (count[c] == 0 ? 1 : 0);
            max = Math.max(max, currentMax);
        }

        bw.write(String.valueOf(max));
        bw.flush();
        bw.close();
        br.close();
    }
}