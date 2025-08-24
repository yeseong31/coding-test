import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.StringTokenizer;

public class Main {

    private static void swap(char[] arr, int a, int b) {
        char tmp = arr[a];
        arr[a] = arr[b];
        arr[b] = tmp;
    }

    private static boolean np(char[] arr) {
        int n = arr.length;

        int i = n - 1;
        while (i > 0 && arr[i - 1] >= arr[i]) i--;
        if (i == 0) return false;

        int j = n - 1;
        while (arr[i - 1] >= arr[j]) j--;
        swap(arr, i - 1, j);

        int k = n - 1;
        while (i < k) swap(arr, i++, k--);
        return true;
    }

    private static String solution(char[] arr, int seq) {
        int count = 1;

        do {
            if (count++ == seq) return new String(arr);
        } while (np(arr));

        return "No permutation";
    }

    public static void main(String[] args) throws Exception {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringBuilder sb = new StringBuilder();

        String line;
        while ((line = br.readLine()) != null) {
            line = line.trim();
            if (line.isEmpty()) continue;

            StringTokenizer st = new StringTokenizer(line);
            String s = st.nextToken();
            char[] arr = s.toCharArray();
            int seq = Integer.parseInt(st.nextToken());

            String message = String.format("%s %s = %s", s, seq, solution(arr, seq));
            sb.append(message).append("\n");
        }

        bw.write(sb.toString());
        bw.flush();
        bw.close();
    }
}