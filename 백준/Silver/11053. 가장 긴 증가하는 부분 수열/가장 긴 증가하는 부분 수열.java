import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());
        int[] numbers = new int[n];

        StringTokenizer st = new StringTokenizer(br.readLine());
        for (int i = 0; i < n; i++) {
            numbers[i] = Integer.parseInt(st.nextToken());
        }

        int answer = solution(n, numbers);
        System.out.println(answer);
        br.close();
    }

    private static int solution(int n, int[] numbers) {
        int[] tails = new int[n];
        int size = 0;

        for (int num : numbers) {
            int idx = Arrays.binarySearch(tails, 0, size, num);
            if (idx < 0) {
                idx = -(idx + 1);
            }
            tails[idx] = num;
            if (idx == size) size++;
        }

        return size;
    }
}
