import java.io.*;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.StringTokenizer;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringBuilder sb = new StringBuilder();

        int n = Integer.parseInt(br.readLine());
        int[] arr = new int[n];

        StringTokenizer st = new StringTokenizer(br.readLine());
        for (int i = 0; i < n; i++) {
            arr[i] = Integer.parseInt(st.nextToken());
        }

        int[] answer = solution(n, arr);

        sb.append(answer.length).append("\n");
        for (int x : answer) {
            sb.append(x).append(" ");
        }

        bw.write(sb.toString());
        bw.flush();
        bw.close();
    }

    private static int[] solution(int n, int[] arr) {
        int[] dp = new int[n];    // arr[i]를 끝으로 하는 LIS의 길이
        int[] prev = new int[n];  // arr[i] 앞에 오는 LIS의 이전 인덱스

        Arrays.fill(dp, 1);
        Arrays.fill(prev, -1);

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < i; j++) {
                if (arr[i] > arr[j] && dp[i] < dp[j] + 1) {
                    dp[i] = dp[j] + 1;
                    prev[i] = j;
                }
            }
        }

        // 가장 긴 LIS 길이와 위치 확인
        int maxLen = 0;
        int maxIdx = 0;

        for (int i = 0; i < n; i++) {
            if (dp[i] > maxLen) {
                maxLen = dp[i];
                maxIdx = i;
            }
        }

        // LIS 복원
        List<Integer> answer = new ArrayList<>();
        int currIdx = maxIdx;

        while (currIdx != -1) {
            answer.add(0, arr[currIdx]);
            currIdx = prev[currIdx];
        }

        return answer.stream().mapToInt(x -> x).toArray();
    }
}