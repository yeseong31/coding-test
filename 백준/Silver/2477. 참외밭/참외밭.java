import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.StringTokenizer;

public class Main {

    private static int solution(int kcal, int[][] lines) {
        int maxWidth = 0;
        int maxHeight = 0;
        int maxWidthIdx = 0;
        int maxHeightIdx = 0;

        for (int i = 0; i < 6; i++) {
            if (lines[i][0] == 1 || lines[i][0] == 2) {
                if (lines[i][1] > maxWidth) {
                    maxWidth = lines[i][1];
                    maxWidthIdx = i;
                }
            } else {
                if (lines[i][1] > maxHeight) {
                    maxHeight = lines[i][1];
                    maxHeightIdx = i;
                }
            }
        }

        int smallWidth = Math.abs(lines[(maxHeightIdx + 5) % 6][1] - lines[(maxHeightIdx + 1) % 6][1]);
        int smallHeight = Math.abs(lines[(maxWidthIdx + 5) % 6][1] - lines[(maxWidthIdx + 1) % 6][1]);

        int bigArea = maxWidth * maxHeight;
        int smallArea = smallWidth * smallHeight;

        return (bigArea - smallArea) * kcal;
    }

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringBuilder sb = new StringBuilder();

        int kcal = Integer.parseInt(br.readLine());
        int[][] lines = new int[6][2];

        for (int i = 0; i < 6; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());

            int d = Integer.parseInt(st.nextToken());
            int l = Integer.parseInt(st.nextToken());

            lines[i][0] = d;
            lines[i][1] = l;
        }

        int answer = solution(kcal, lines);
        sb.append(answer);

        bw.write(sb.toString());
        bw.flush();
        bw.close();
    }
}
