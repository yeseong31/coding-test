import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.StringTokenizer;

public class Main {

    private static int[] solution(int n, int[][] info) {
        int[] answer = new int[2];
        int size = 0;
        int tail = 0;

        for (int[] row : info) {
            if (row[0] == 1) {
                size++;
                tail = row[1];
                continue;
            }

            updateAnswer(answer, size--, tail);
        }

        updateAnswer(answer, size, tail);
        return answer;
    }

    private static void updateAnswer(int[] answer, int size, int tail) {
        if (answer[0] > size) return;

        if (answer[0] < size) {
            answer[0] = size;
            answer[1] = tail;
        } else {
            answer[1] = Math.min(answer[1], tail);
        }
    }

    public static void main(String[] args) throws Exception {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringBuilder sb = new StringBuilder();

        int n = Integer.parseInt(br.readLine());

        int[][] info = new int[n][2];
        for (int i = 0; i < n; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            info[i][0] = Integer.parseInt(st.nextToken());

            if (info[i][0] == 1) {
                info[i][1] = Integer.parseInt(st.nextToken());
            }
        }

        int[] answer = solution(n, info);
        sb.append(answer[0]).append(" ").append(answer[1]);

        bw.write(sb.toString());
        bw.flush();
        bw.close();
    }
}