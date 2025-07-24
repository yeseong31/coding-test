import java.io.*;
import java.util.StringTokenizer;

public class Main {

    private static int solution(String s) {
        int sum = 0;
        int max = -1;

        for (char c : s.toCharArray()) {
            switch (c) {
                case '(':
                    sum += 1;
                    break;
                case '{':
                    sum += 2;
                    break;
                case '[':
                    sum += 3;
                    break;
                case ')':
                    sum -= 1;
                    break;
                case '}':
                    sum -= 2;
                    break;
                case ']':
                    sum -= 3;
                    break;
                default:
                    if (Character.isDigit(c)) {
                        max = Math.max(max, sum);
                    }
            }
        }

        return max;
    }

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringBuilder sb = new StringBuilder();

        StringTokenizer st = new StringTokenizer(br.readLine());
        String s = st.nextToken();

        int answer = solution(s);
        sb.append(answer);

        bw.write(sb.toString());
        bw.flush();
        bw.close();
    }
}