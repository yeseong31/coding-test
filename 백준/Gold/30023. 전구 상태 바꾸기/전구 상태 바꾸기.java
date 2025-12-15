import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;

public class Main {

    private static final Map<Character, Integer> colorMap = new HashMap<>();

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());
        int[] colors = new int[n];

        colorMap.put('R', 0);
        colorMap.put('G', 1);
        colorMap.put('B', 2);

        int seq = 0;
        for (char c : br.readLine().toCharArray()) {
            colors[seq++] = colorMap.get(c);
        }

        int answer = Integer.MAX_VALUE;
        answer = Math.min(answer, count(0, n, colors));
        answer = Math.min(answer, count(1, n, colors));
        answer = Math.min(answer, count(2, n, colors));

        System.out.println(answer == Integer.MAX_VALUE ? -1 : answer);
    }

    private static int count(int target, int n, int[] originColors) {
        int[] colors = Arrays.copyOf(originColors, n);
        int result = 0;

        for (int i = 0; i <= n - 3; i++) {
            if (colors[i] == target) {
                continue;
            }

            int cnt = (target - colors[i] + 3) % 3;
            result += cnt;

            for (int j = 0; j < 3; j++) {
                colors[i + j] += cnt;
                if (colors[i + j] >= 3) {
                    colors[i + j] -= 3;
                }
            }
        }

        for (int i = n - 2; i < n; i++) {
            if (colors[i] != target) {
                return Integer.MAX_VALUE;
            }
        }

        return result;
    }
}