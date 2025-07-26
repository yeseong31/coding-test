import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.StringTokenizer;

public class Main {

    private static void rotate(int n, int[] arr) {
        int temp = arr[2 * n - 1];
        
        for (int i = 2 * n - 1; i > 0; i--) {
            arr[i] = arr[i - 1];
        }
        
        arr[0] = temp;
    }

    private static void rotate(int n, boolean[] arr) {
        boolean temp = arr[2 * n - 1];
        
        for (int i = 2 * n - 1; i > 0; i--) {
            arr[i] = arr[i - 1];
        }
        
        arr[0] = temp;
    }

    private static int move(int n, int[] belt, boolean[] robots) {
        int count = 0;

        for (int i = n - 2; i >= 0; i--) {
            if (!robots[i] || robots[i + 1] || belt[i + 1] <= 0) {
                continue;
            }

            robots[i] = false;
            robots[i + 1] = true;

            if (--belt[i + 1] == 0) {
                count++;
            }
        }

        return count;
    }

    private static int solution(int n, int k, int[] belt) {
        int seq = 0;

        boolean[] robots = new boolean[2 * n];

        while (k > 0) {
            seq++;

            rotate(n, belt);
            rotate(n, robots);
            robots[n - 1] = false;

            k -= move(n, belt, robots);
            robots[n - 1] = false;

            if (belt[0] > 0 && !robots[0]) {
                robots[0] = true;

                if (--belt[0] == 0) {
                    k--;
                }
            }
        }

        return seq;
    }

    public static void main(String[] args) throws Exception {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringBuilder sb = new StringBuilder();

        StringTokenizer st = new StringTokenizer(br.readLine());
        
        int n = Integer.parseInt(st.nextToken());
        int k = Integer.parseInt(st.nextToken());

        st = new StringTokenizer(br.readLine());
        
        int[] belt = new int[2 * n];
        for (int i = 0; i < 2 * n; i++) {
            belt[i] = Integer.parseInt(st.nextToken());
        }

        int answer = solution(n, k, belt);

        sb.append(answer);
        bw.write(sb.toString());
        bw.flush();
        bw.close();
    }
}