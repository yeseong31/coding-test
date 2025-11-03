import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.Arrays;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringBuilder sb = new StringBuilder();

        int n = Integer.parseInt(br.readLine());
        char[] road = br.readLine().toCharArray();

        sb.append(solution(n, road));
        bw.write(sb.toString());
        bw.flush();
        bw.close();
    }

    private static long solution(int n, char[] road) {
        Map<List<Integer>, Long> counts = new HashMap<>();
        counts.put(Arrays.asList(0, 0, 0, 0), 1L);

        int t = 0, g = 0, f = 0, p = 0;
        Long result = 0L;

        for (char ch : road) {
            if (ch == 'T') {
                t++;
            }
            if (ch == 'G') {
                g++;
            }
            if (ch == 'F') {
                f++;
            }
            if (ch == 'P') {
                p++;
            }

            List<Integer> state = Arrays.asList(t % 3, g % 3, f % 3, p % 3);
            result += counts.getOrDefault(state, 0L);
            counts.put(state, counts.getOrDefault(state, 0L) + 1);
        }

        return result;
    }
}