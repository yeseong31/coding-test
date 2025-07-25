import java.io.*;
import java.util.StringTokenizer;

public class Main {

    private static int solution(String s) {
        int answer = Integer.MIN_VALUE;
        int score = 0;

        for (char c : s.toCharArray()) {
            switch (c) {
                case '(': score += 1; break;
                case ')': score -= 1; break;
                case '{': score += 2; break;
                case '}': score -= 2; break;
                case '[': score += 3; break;
                case ']': score -= 3; break;
                default: {
                    if (Character.isDigit(c)) {
                        answer = Math.max(answer, score);
                    }
                } break;
            }
        }

        return answer;
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