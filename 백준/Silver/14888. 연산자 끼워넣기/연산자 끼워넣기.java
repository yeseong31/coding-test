import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.*;

public class Main {

    private static final char[] operations = {'+', '-', '*', '/'};
    private static final Map<Character, Integer> opMap = new HashMap<>();

    private static void swap(char[] arr, int a, int b) {
        char tmp = arr[a];
        arr[a] = arr[b];
        arr[b] = tmp;
    }

    private static boolean np(char[] arr) {
        int n = arr.length;

        int i = n - 1;
        while (i > 0 && opMap.get(arr[i - 1]) >= opMap.get(arr[i])) i--;
        if (i == 0) return false;

        int j = n - 1;
        while (opMap.get(arr[i - 1]) >= opMap.get(arr[j])) j--;
        swap(arr, i - 1, j);

        int k = n - 1;
        while (i < k) swap(arr, i++, k--);
        return true;
    }

    private static int calculate(int[] a, char[] ops) {
        int result = a[0];

        for (int i = 0; i < ops.length; i++) {
            switch (ops[i]) {
                case '+': result += a[i + 1]; break;
                case '-': result -= a[i + 1]; break;
                case '*': result *= a[i + 1]; break;
                case '/': result /= a[i + 1]; break;
            }
        }

        return result;
    }

    private static int[] solution(int n, int[] a, char[] ops) {
        int maxValue = Integer.MIN_VALUE;
        int minValue = Integer.MAX_VALUE;

        do {
            int value = calculate(a, ops);
            maxValue = Math.max(maxValue, value);
            minValue = Math.min(minValue, value);
        } while (np(ops));

        return new int[]{maxValue, minValue};
    }

    public static void main(String[] args) throws Exception {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringBuilder sb = new StringBuilder();

        int n = Integer.parseInt(br.readLine());

        StringTokenizer st = new StringTokenizer(br.readLine());
        int[] a = new int[n];
        for (int i = 0; i < n; i++) {
            a[i] = Integer.parseInt(st.nextToken());
        }

        st = new StringTokenizer(br.readLine());
        List<Character> combinations = new ArrayList<>();

        for (int i = 0; i < 4; i++) {
            int count = Integer.parseInt(st.nextToken());
            for (int j = 0; j < count; j++){
                combinations.add(operations[i]);
            }
            opMap.put(operations[i], i);
        }

        char[] arr = new char[combinations.size()];
        for (int i = 0; i < combinations.size(); i++) {
            arr[i] = combinations.get(i);
        }

        int[] answer = solution(n, a, arr);
        sb.append(answer[0]).append("\n").append(answer[1]);

        bw.write(sb.toString());
        bw.flush();
        bw.close();
    }
}