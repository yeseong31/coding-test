import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.StringTokenizer;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringBuilder sb = new StringBuilder();

        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());

        int[] numbers = new int[n];
        for (int i = 0; i < n; i++) {
            numbers[i] = i + 1;
        }

        for (int k = 0; k < m; k++) {
            st = new StringTokenizer(br.readLine());
            int i = Integer.parseInt(st.nextToken());
            int j = Integer.parseInt(st.nextToken());

            if (i == j) {
                continue;
            }

            int l = i - 1;
            int r = j - 1;
            while (l < r) {
                swap(numbers, l++, r--);
            }
        }

        for (int number : numbers) {
            sb.append(number).append(" ");
        }

        bw.write(sb.toString());
        bw.flush();
        bw.close();
        br.close();
    }

    private static void swap(int[] numbers, int i, int j) {
        int temp = numbers[i];
        numbers[i] = numbers[j];
        numbers[j] = temp;
    }
}