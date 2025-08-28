import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.StringTokenizer;

public class Main {
    
    private static long solution(long a, long b, long c) {
        if (b == 1) return a % c;

        long result = solution(a, b / 2, c);

        if (b % 2 == 0) {
            return (result * result) % c;
        }
        return ((result * result) % c * a) % c;
    }

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringBuilder sb = new StringBuilder();

        StringTokenizer st = new StringTokenizer(br.readLine());
        long a = Integer.parseInt(st.nextToken());
        long b = Integer.parseInt(st.nextToken());
        long c = Integer.parseInt(st.nextToken());
        long answer = solution(a, b, c);

        sb.append(answer);
        bw.write(sb.toString());
        bw.flush();
        bw.close();
    }
}