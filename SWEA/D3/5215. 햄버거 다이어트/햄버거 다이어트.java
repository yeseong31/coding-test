import java.io.*;
import java.util.StringTokenizer;

public class Solution {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringBuilder sb = new StringBuilder();

        int T = Integer.parseInt(br.readLine());

        for (int testCase = 1; testCase <= T; testCase++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int n = Integer.parseInt(st.nextToken());
            int l = Integer.parseInt(st.nextToken());

            int[][] ingredients = new int[n][2];
            for (int i = 0; i < n; i++) {
                st = new StringTokenizer(br.readLine());
                ingredients[i][0] = Integer.parseInt(st.nextToken());
                ingredients[i][1] = Integer.parseInt(st.nextToken());
            }

            int[] hamburgers = new int[l + 1];
            for (int i = 0; i < n; i++) {
                for (int kcal = l; kcal >= ingredients[i][1]; kcal--) {
                    hamburgers[kcal] = Math.max(hamburgers[kcal], ingredients[i][0] + hamburgers[kcal - ingredients[i][1]]);
                }
            }

            sb.append("#").append(testCase).append(" ").append(hamburgers[l]).append("\n");
        }

        bw.write(sb.toString());
        bw.flush();
        bw.close();
        br.close();
    }
}