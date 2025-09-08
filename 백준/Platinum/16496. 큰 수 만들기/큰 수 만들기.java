import java.io.*;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringBuilder sb = new StringBuilder();

        int n = Integer.parseInt(br.readLine());

        StringTokenizer st = new StringTokenizer(br.readLine());

        String[] tokens = new String[n];
        for (int i = 0; i < n; i++) {
            tokens[i] = st.nextToken();
        }

        Arrays.sort(tokens, (a, b) -> (b + a).compareTo(a + b));

        for (int i = 0; i < n; i++) {
            sb.append(tokens[i]);
        }

        if (sb.charAt(0) == '0') {
            System.out.println('0');
        } else {
            bw.write(sb.toString());
        }

        bw.flush();
        bw.close();
    }
}