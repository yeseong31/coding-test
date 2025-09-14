import java.io.*;
import java.util.*;

public class Main {

    private static int n;
    private static int[] arr;
    private static int[] opCount; // +, -, *, /
    private static long max = Long.MIN_VALUE;
    private static long min = Long.MAX_VALUE;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        n = Integer.parseInt(br.readLine());

        StringTokenizer st = new StringTokenizer(br.readLine());
        arr = new int[n];
        for (int i = 0; i < n; i++) {
            arr[i] = Integer.parseInt(st.nextToken());
        }

        st = new StringTokenizer(br.readLine());
        opCount = new int[4];
        for (int i = 0; i < 4; i++) {
            opCount[i] = Integer.parseInt(st.nextToken());
        }

        dfs(1, new ArrayList<>(), new ArrayList<>());

        System.out.println(max);
        System.out.println(min);
    }

    private static void dfs(int depth, List<Integer> nums, List<Character> ops) {
        if (depth == n) {
            nums.add(arr[depth - 1]);
            long result = evaluate(nums, ops);
            max = Math.max(max, result);
            min = Math.min(min, result);
            nums.remove(nums.size() - 1);
            return;
        }

        nums.add(arr[depth - 1]);

        for (int i = 0; i < 4; i++) {
            if (opCount[i] > 0) {
                opCount[i]--;
                ops.add(toOp(i));
                dfs(depth + 1, nums, ops);
                ops.remove(ops.size() - 1);
                opCount[i]++;
            }
        }

        nums.remove(nums.size() - 1);
    }

    private static char toOp(int idx) {
        switch (idx) {
            case 0: return '+';
            case 1: return '-';
            case 2: return '*';
            default: return '/';
        }
    }

    private static long evaluate(List<Integer> nums, List<Character> ops) {
        List<Long> numList = new ArrayList<>();
        List<Character> opList = new ArrayList<>();
        numList.add((long) nums.get(0));

        for (int i = 0; i < ops.size(); i++) {
            char op = ops.get(i);
            long b = nums.get(i + 1);

            if (op == '*' || op == '/') {
                long a = numList.remove(numList.size() - 1);
                numList.add(calc(a, b, op));
            } else {
                numList.add(b);
                opList.add(op);
            }
        }

        long result = numList.get(0);
        for (int i = 0; i < opList.size(); i++) {
            result = calc(result, numList.get(i + 1), opList.get(i));
        }

        return result;
    }

    private static long calc(long a, long b, char op) {
        switch (op) {
            case '+': return a + b;
            case '-': return a - b;
            case '*': return a * b;
            case '/':
                if (a < 0) return -((-a) / b);
                else return a / b;
        }
        return 0;
    }
}