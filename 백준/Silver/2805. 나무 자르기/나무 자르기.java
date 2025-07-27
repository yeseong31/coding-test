import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {

    private static long solution(int n, long m, long[] trees) {
        long answer = 0;

        Arrays.sort(trees);

        long left = 0;
        long right = trees[n - 1] + 1;

        while (left < right) {
            long mid = (left + right) / 2;
            long treeSum = 0;

            for (long tree : trees) {
                if (tree - mid < 0) continue;
                if (treeSum >= m) break;
                treeSum += tree - mid;
            }

            if (treeSum >= m) {
                answer = mid;
                left = mid + 1;
            } else {
                right = mid;
            }
        }

        return answer;
    }

    public static void main(String[] args) throws Exception {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringBuilder sb = new StringBuilder();

        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        long m = Integer.parseInt(st.nextToken());

        long[] trees = new long[n];
        st = new StringTokenizer(br.readLine());

        for (int i = 0; i < n; i++) {
            trees[i] = Long.parseLong(st.nextToken());
        }

        long answer = solution(n, m, trees);
        sb.append(answer);

        bw.write(sb.toString());
        bw.flush();
        bw.close();
    }
}