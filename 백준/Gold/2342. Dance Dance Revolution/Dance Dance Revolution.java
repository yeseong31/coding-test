import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.StringTokenizer;

public class Main {

    private static final int INF = Integer.MAX_VALUE;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        List<Integer> numbers = new ArrayList<>();
        while (st.hasMoreTokens()) {
            int n = Integer.parseInt(st.nextToken());
            if (n == 0) {
                System.out.println(solution(numbers));
                return;
            }
            numbers.add(n);
        }
    }

    private static int solution(List<Integer> numbers) {
        int n = numbers.size();
        int[][] currDp = new int[5][5];
        int[][] nextDp = new int[5][5];

        for (int i = 0; i < 5; i++) {
            Arrays.fill(currDp[i], INF);
        }
        currDp[0][0] = 0;

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < 5; j++) {
                Arrays.fill(nextDp[j], INF);
            }

            int p = numbers.get(i);

            for (int l = 0; l < 5; l++) {
                for (int r = 0; r < 5; r++) {
                    int cost = currDp[l][r];
                    if (cost == INF) {
                        continue;
                    }

                    int leftCost = calculate(l, p);
                    if (cost + leftCost < nextDp[p][r]) {
                        nextDp[p][r] = cost + leftCost;
                    }

                    int rightCost = calculate(r, p);
                    if (cost + rightCost < nextDp[l][p]) {
                        nextDp[l][p] = cost + rightCost;
                    }
                }
            }

            int[][] tmp = currDp;
            currDp = nextDp;
            nextDp = tmp;
        }

        int answer = INF;
        for (int l = 0; l < 5; l++) {
            for (int r = 0; r < 5; r++) {
                answer = Math.min(answer, currDp[l][r]);
            }
        }
        return answer;
    }

    private static int calculate(int prev, int next) {
        if (prev == 0) {
            return 2;
        }
        if (prev == next) {
            return 1;
        }
        if (Math.abs(next - prev) == 2) {
            return 4;
        }
        return 3;
    }
}